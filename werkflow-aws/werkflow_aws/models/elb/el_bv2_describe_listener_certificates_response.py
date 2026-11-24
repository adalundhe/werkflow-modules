from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .el_bv2_certificate import ELBv2Certificate


class ELBv2DescribeListenerCertificatesResponse(BaseModel):
    Certificates: list[ELBv2Certificate] | None = None
    NextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
