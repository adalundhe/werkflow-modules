import datetime
from pydantic import BaseModel, StrictStr


class AWSs3BucketResponse(BaseModel):
    Name: StrictStr
    CreationDate: datetime.datetime
    