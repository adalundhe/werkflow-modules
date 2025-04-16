from pydantic import BaseModel, StrictStr


class Tag(BaseModel):
    Key: StrictStr
    Value: StrictStr