from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetails(BaseModel):
    Count: StrictInt | None = None
    Type: StrictStr | None = None
