import datetime
from pydantic import BaseModel, StrictStr


class AWSs3BucketResponse(BaseModel):
    Name: StrictStr | None = None
    CreationDate: datetime.datetime | None = None
    
