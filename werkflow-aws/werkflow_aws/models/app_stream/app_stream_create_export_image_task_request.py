from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamCreateExportImageTaskRequest(BaseModel):
    ImageName: StrictStr
    AmiName: StrictStr
    IamRoleArn: StrictStr
    TagSpecifications: dict[StrictStr, StrictStr] | None = None
    AmiDescription: StrictStr | None = None
