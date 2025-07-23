from pydantic import BaseModel, StrictStr, StrictInt, Field
from typing import Optional
from datetime import datetime


class BookResponseModel(BaseModel):
    id: StrictInt
    title: StrictStr
    description: Optional[StrictStr]
    pageCount: StrictInt = Field(gt=0)
    excerpt: Optional[StrictStr]
    publishDate: datetime
