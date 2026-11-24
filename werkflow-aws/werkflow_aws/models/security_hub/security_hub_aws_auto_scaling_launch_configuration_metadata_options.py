from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsAutoScalingLaunchConfigurationMetadataOptions(BaseModel):
    HttpEndpoint: StrictStr | None = None
    HttpPutResponseHopLimit: StrictInt | None = None
    HttpTokens: StrictStr | None = None
