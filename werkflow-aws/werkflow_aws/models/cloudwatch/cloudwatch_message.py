from pydantic import BaseModel, StrictStr


class CloudWatchMessage(BaseModel):
    Code: StrictStr
    Value: StrictStr