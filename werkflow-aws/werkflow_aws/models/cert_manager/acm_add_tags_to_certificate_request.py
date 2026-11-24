from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .acm_tag import ACMTag


class ACMAddTagsToCertificateRequest(BaseModel):
    CertificateArn: StrictStr
    Tags: list[ACMTag]
