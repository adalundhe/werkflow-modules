from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTCertificateProviderSummary(BaseModel):
    certificateProviderName: StrictStr | None = None
    certificateProviderArn: StrictStr | None = None
