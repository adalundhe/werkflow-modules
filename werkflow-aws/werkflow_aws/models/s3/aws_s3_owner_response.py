from pydantic import BaseModel, StrictStr


class AWSs3OwnerResponse(BaseModel):
    DisplayName: StrictStr
    ID: StrictStr