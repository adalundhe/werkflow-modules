from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEc2LaunchTemplateDataLicenseSetDetails(BaseModel):
    LicenseConfigurationArn: StrictStr | None = None
