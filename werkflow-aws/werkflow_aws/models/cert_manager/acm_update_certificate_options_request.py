from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .acm_certificate_options import ACMCertificateOptions


class ACMUpdateCertificateOptionsRequest(BaseModel):
    CertificateArn: StrictStr
    Options: ACMCertificateOptions
