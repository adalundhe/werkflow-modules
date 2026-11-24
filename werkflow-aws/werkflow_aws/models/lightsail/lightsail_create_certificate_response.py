from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lightsail_certificate_summary import LightsailCertificateSummary
from .lightsail_operation import LightsailOperation


class LightsailCreateCertificateResponse(BaseModel):
    certificate: LightsailCertificateSummary | None = None
    operations: list[LightsailOperation] | None = None
    ResponseMetadata: dict[str, Any] | None = None
