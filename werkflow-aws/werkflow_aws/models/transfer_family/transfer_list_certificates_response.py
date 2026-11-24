from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .transfer_listed_certificate import TransferListedCertificate


class TransferListCertificatesResponse(BaseModel):
    NextToken: StrictStr | None = None
    Certificates: list[TransferListedCertificate] | None = None
    ResponseMetadata: dict[str, Any] | None = None
