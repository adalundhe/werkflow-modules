from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailAttachCertificateToDistributionRequest(BaseModel):
    distributionName: StrictStr
    certificateName: StrictStr
