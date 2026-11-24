from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_certificate_provider_summary import IoTCertificateProviderSummary


class IoTListCertificateProvidersResponse(BaseModel):
    certificateProviders: list[IoTCertificateProviderSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
