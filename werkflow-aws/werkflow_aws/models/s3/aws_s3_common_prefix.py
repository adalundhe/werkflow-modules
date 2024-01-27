from pydantic import BaseModel, StrictStr


class AWSs3CommonPrefix(BaseModel):
    Prefix: StrictStr