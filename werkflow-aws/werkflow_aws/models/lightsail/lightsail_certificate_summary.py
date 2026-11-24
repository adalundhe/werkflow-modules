from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lightsail_certificate import LightsailCertificate
from .lightsail_tag import LightsailTag


class LightsailCertificateSummary(BaseModel):
    certificateArn: StrictStr | None = None
    certificateName: StrictStr | None = None
    domainName: StrictStr | None = None
    certificateDetail: LightsailCertificate | None = None
    tags: list[LightsailTag] | None = None
