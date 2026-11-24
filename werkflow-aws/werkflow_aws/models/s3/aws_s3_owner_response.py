from pydantic import BaseModel, StrictStr


class AWSs3OwnerResponse(BaseModel):
    DisplayName: StrictStr | None = None
    ID: StrictStr | None = None
