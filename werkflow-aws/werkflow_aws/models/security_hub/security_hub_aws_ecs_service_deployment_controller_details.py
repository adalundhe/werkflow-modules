from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEcsServiceDeploymentControllerDetails(BaseModel):
    Type: StrictStr | None = None
