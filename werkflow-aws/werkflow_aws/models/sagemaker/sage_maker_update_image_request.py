from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerUpdateImageRequest(BaseModel):
    ImageName: StrictStr
    DeleteProperties: list[StrictStr] | None = None
    Description: StrictStr | None = None
    DisplayName: StrictStr | None = None
    RoleArn: StrictStr | None = None
