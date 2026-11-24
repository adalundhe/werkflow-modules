from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_available_number_summary import ConnectAvailableNumberSummary


class ConnectSearchAvailablePhoneNumbersResponse(BaseModel):
    NextToken: StrictStr | None = None
    AvailableNumbersList: list[ConnectAvailableNumberSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
