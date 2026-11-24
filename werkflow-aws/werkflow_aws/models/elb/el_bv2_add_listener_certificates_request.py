from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .el_bv2_certificate import ELBv2Certificate


class ELBv2AddListenerCertificatesRequest(BaseModel):
    ListenerArn: StrictStr
    Certificates: list[ELBv2Certificate]
