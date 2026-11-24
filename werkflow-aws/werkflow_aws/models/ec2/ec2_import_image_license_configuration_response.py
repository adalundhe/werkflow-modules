from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2ImportImageLicenseConfigurationResponse(BaseModel):
    LicenseConfigurationArn: StrictStr | None = None
