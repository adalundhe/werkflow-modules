from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LakeFormationAssumeDecoratedRoleWithSAMLRequest(BaseModel):
    SAMLAssertion: StrictStr
    RoleArn: StrictStr
    PrincipalArn: StrictStr
    DurationSeconds: StrictInt | None = None
