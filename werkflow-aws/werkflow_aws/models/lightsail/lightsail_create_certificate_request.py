from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lightsail_tag import LightsailTag


class LightsailCreateCertificateRequest(BaseModel):
    certificateName: StrictStr
    domainName: StrictStr
    subjectAlternativeNames: list[StrictStr] | None = None
    tags: list[LightsailTag] | None = None
