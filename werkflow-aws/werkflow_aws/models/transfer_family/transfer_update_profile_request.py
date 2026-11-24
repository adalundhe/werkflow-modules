from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferUpdateProfileRequest(BaseModel):
    ProfileId: StrictStr
    CertificateIds: list[StrictStr] | None = None
