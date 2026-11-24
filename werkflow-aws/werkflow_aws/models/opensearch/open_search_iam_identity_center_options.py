from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class OpenSearchIamIdentityCenterOptions(BaseModel):
    enabled: StrictBool | None = None
    iamIdentityCenterInstanceArn: StrictStr | None = None
    iamRoleForIdentityCenterApplicationArn: StrictStr | None = None
    iamIdentityCenterApplicationArn: StrictStr | None = None
