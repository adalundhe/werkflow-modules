from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDescribeCertificateProviderRequest(BaseModel):
    certificateProviderName: StrictStr
