from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .transfer_described_certificate import TransferDescribedCertificate


class TransferDescribeCertificateResponse(BaseModel):
    Certificate: TransferDescribedCertificate | None = None
    ResponseMetadata: dict[str, Any] | None = None
