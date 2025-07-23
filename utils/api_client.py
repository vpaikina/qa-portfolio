import requests
from config.env_config import BASE_URL


class APIClient:
    """
    A reusable API client wrapper around the requests library
    """

    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()

    def _build_url(self, endpoint: str) -> str:
        return f"{self.base_url}/{endpoint.lstrip('/')}"

    def _log_request(self, method: str, url: str, **kwargs):
        print(f"[REQUEST] {method} {url}")
        if "json" in kwargs:
            print(f"Payload: {kwargs['json']}")
        if "params" in kwargs:
            print(f"Params: {kwargs['params']}")

    def _log_response(self, response: requests.Response):
        print(f"[RESPONSE] Status: {response.status_code}")
        try:
            print(f"Response JSON: {response.json()}")
        except Exception:
            print(f"Response Text: {response.text}")

    def request(
        self,
        method: str,
        endpoint: str,
        expected_status: int = 200,
        error_message: str = None,
        **kwargs,
    ) -> requests.Response:
        url = self._build_url(endpoint)
        self._log_request(method, url, **kwargs)
        response = self.session.request(method=method, url=url, **kwargs)
        self._log_response(response)
        if response.status_code != expected_status:
            base_msg = (
                f"Expected status {expected_status}, got {response.status_code}\n"
                f"URL: {url}\n"
                f"Response: {getattr(response, 'text', '')}"
            )
            if error_message:
                base_msg = f"{error_message}\n{base_msg}"
            raise AssertionError(base_msg)
        return response

    def get(self, endpoint: str, **kwargs) -> requests.Response:
        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs) -> requests.Response:
        return self.request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs) -> requests.Response:
        return self.request("PUT", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        return self.request("DELETE", endpoint, **kwargs)
