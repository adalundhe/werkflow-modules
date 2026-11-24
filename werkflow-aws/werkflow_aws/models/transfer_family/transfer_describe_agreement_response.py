from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .transfer_described_agreement import TransferDescribedAgreement


class TransferDescribeAgreementResponse(BaseModel):
    Agreement: TransferDescribedAgreement | None = None
    ResponseMetadata: dict[str, Any] | None = None
