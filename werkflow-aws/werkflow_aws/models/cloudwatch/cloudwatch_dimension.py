from pydantic import BaseModel, StrictStr


class CloudWatchDimension(BaseModel):
    Name: StrictStr
    Value: StrictStr