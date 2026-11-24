from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_claimed_phone_number_summary import ConnectClaimedPhoneNumberSummary


class ConnectDescribePhoneNumberResponse(BaseModel):
    ClaimedPhoneNumberSummary: ConnectClaimedPhoneNumberSummary | None = None
    ResponseMetadata: dict[str, Any] | None = None
