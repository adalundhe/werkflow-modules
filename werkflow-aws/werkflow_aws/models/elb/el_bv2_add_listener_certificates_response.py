from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .el_bv2_certificate import ELBv2Certificate


class ELBv2AddListenerCertificatesResponse(BaseModel):
    Certificates: list[ELBv2Certificate] | None = None
    ResponseMetadata: dict[str, Any] | None = None
