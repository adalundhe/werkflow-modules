from __future__ import annotations
from pydantic import BaseModel
from .security_hub_aws_ssm_compliance_summary import SecurityHubAwsSsmComplianceSummary


class SecurityHubAwsSsmPatch(BaseModel):
    ComplianceSummary: SecurityHubAwsSsmComplianceSummary | None = None
