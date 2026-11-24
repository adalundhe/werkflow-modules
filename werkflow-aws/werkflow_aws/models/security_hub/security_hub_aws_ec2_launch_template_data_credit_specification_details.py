from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEc2LaunchTemplateDataCreditSpecificationDetails(BaseModel):
    CpuCredits: StrictStr | None = None
