from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class OpenSearchIamIdentityCenterOptionsInput(BaseModel):
    enabled: StrictBool | None = None
    iamIdentityCenterInstanceArn: StrictStr | None = None
    iamRoleForIdentityCenterApplicationArn: StrictStr | None = None
