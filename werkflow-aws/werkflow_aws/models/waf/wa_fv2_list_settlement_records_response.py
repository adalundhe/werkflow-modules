from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .wa_fv2_settlement_record import WAFv2SettlementRecord


class WAFv2ListSettlementRecordsResponse(BaseModel):
    Settlements: list[WAFv2SettlementRecord] | None = None
    NextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
