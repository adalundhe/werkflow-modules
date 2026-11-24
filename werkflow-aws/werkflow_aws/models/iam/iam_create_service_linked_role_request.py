from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMCreateServiceLinkedRoleRequest(BaseModel):
    AWSServiceName: StrictStr
    Description: StrictStr | None = None
    CustomSuffix: StrictStr | None = None
