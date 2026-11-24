from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubRemediationGuidanceExamples(BaseModel):
    AwsCli: StrictStr | None = None
    Cli: StrictStr | None = None
    Python: StrictStr | None = None
    Terraform: StrictStr | None = None
    Cdk: StrictStr | None = None
    CloudFormation: StrictStr | None = None
    IaC: StrictStr | None = None
    Template: StrictStr | None = None
