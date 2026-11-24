from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsS3AccessPointVpcConfigurationDetails(BaseModel):
    VpcId: StrictStr | None = None
