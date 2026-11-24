from __future__ import annotations
from pydantic import BaseModel
from .security_hub_aws_ssm_patch import SecurityHubAwsSsmPatch


class SecurityHubAwsSsmPatchComplianceDetails(BaseModel):
    Patch: SecurityHubAwsSsmPatch | None = None
