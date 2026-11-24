from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDescribeCACertificateRequest(BaseModel):
    certificateId: StrictStr
