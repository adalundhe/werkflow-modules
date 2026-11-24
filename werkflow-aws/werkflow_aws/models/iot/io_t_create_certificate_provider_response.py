from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IoTCreateCertificateProviderResponse(BaseModel):
    certificateProviderName: StrictStr | None = None
    certificateProviderArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
