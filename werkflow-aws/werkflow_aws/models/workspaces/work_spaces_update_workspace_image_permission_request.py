from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class WorkSpacesUpdateWorkspaceImagePermissionRequest(BaseModel):
    ImageId: StrictStr
    AllowCopyImage: StrictBool
    SharedAccountId: StrictStr
