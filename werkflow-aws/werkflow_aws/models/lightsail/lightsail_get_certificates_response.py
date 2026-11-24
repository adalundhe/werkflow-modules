from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_certificate_summary import LightsailCertificateSummary


class LightsailGetCertificatesResponse(BaseModel):
    certificates: list[LightsailCertificateSummary] | None = None
    nextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
