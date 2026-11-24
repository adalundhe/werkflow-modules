from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetails(BaseModel):
    Type: StrictStr | None = None
