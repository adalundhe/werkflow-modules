from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsRedshiftClusterIamRole(BaseModel):
    ApplyStatus: StrictStr | None = None
    IamRoleArn: StrictStr | None = None
