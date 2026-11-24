from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsIamPolicyVersion(BaseModel):
    VersionId: StrictStr | None = None
    IsDefaultVersion: StrictBool | None = None
    CreateDate: StrictStr | None = None
