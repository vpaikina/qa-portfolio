from contextlib import contextmanager

class ResourceTracker:
    """
    Tracks creation and deletion of resources.
    Automatically cleans up remaining resources at the end of the test
    """

    def __init__(self, delete_func):
        self.created_ids = set()
        self.deleted_ids = set()
        self.delete_func = delete_func

    def track_create(self, resource_id):
        self.created_ids.add(resource_id)

    def track_delete(self, resource_id):
        self.deleted_ids.add(resource_id)

    def cleanup(self):
        for resource_id in list(self.created_ids - self.deleted_ids):
            try:
                resp = self.delete_func(resource_id)
                # Only log warning if not OK or NotFound
                if hasattr(resp, "status_code") and resp.status_code not in (200, 204, 404):
                    print(f"Warning: unexpected status code on cleanup DELETE {resource_id}: {resp.status_code}")
            except Exception as e:
                print(f"Warning: could not delete resource {resource_id}: {e}")

@contextmanager
def tracked_client(api_client, resource_name="books"):
    """
    Wraps api_client to automatically track created and deleted resources.
    """
    tracker = ResourceTracker(lambda rid: api_client.delete(f"/{resource_name}/{rid}", expected_status=200))
    original_post = api_client.post
    original_delete = api_client.delete

    def tracked_post(endpoint, **kwargs):
        response = original_post(endpoint, **kwargs)
        if endpoint == f"/{resource_name}" and response.status_code in (200, 201):
            try:
                resource_id = response.json()["id"]
                tracker.track_create(resource_id)
            except Exception:
                pass  # Could add warning here
        return response

    def tracked_delete(endpoint, **kwargs):
        if endpoint.startswith(f"/{resource_name}/"):
            resource_id = endpoint.split("/")[-1]
            tracker.track_delete(int(resource_id) if resource_id.isdigit() else resource_id)
        return original_delete(endpoint, **kwargs)

    api_client.post = tracked_post
    api_client.delete = tracked_delete

    try:
        yield api_client, tracker
    finally:
        tracker.cleanup()
        api_client.post = original_post
        api_client.delete = original_delete
