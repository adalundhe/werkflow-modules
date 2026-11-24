from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .event_bridge_partner_event_source_account import EventBridgePartnerEventSourceAccount


class EventBridgeListPartnerEventSourceAccountsResponse(BaseModel):
    PartnerEventSourceAccounts: list[EventBridgePartnerEventSourceAccount] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
