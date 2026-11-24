from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rds_certificate import RDSCertificate


class RDSModifyCertificatesResponse(BaseModel):
    Certificate: RDSCertificate | None = None
    ResponseMetadata: dict[str, Any] | None = None
