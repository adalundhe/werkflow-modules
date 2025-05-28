from pydantic import BaseModel, StrictStr


class EC2Tag(BaseModel):
    NAme: StrictStr
    Value: StrictStr