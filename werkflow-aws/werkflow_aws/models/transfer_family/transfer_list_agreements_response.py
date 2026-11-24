from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .transfer_listed_agreement import TransferListedAgreement


class TransferListAgreementsResponse(BaseModel):
    NextToken: StrictStr | None = None
    Agreements: list[TransferListedAgreement] | None = None
    ResponseMetadata: dict[str, Any] | None = None
