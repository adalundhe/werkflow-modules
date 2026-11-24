from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2LaunchTemplateLicenseConfigurationRequest(BaseModel):
    LicenseConfigurationArn: StrictStr | None = None
