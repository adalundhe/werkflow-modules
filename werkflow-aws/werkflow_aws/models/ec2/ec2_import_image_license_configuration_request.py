from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2ImportImageLicenseConfigurationRequest(BaseModel):
    LicenseConfigurationArn: StrictStr | None = None
