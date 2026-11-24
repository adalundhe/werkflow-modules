from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_phone_number_summary import ConnectPhoneNumberSummary


class ConnectListPhoneNumbersResponse(BaseModel):
    PhoneNumberSummaryList: list[ConnectPhoneNumberSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
