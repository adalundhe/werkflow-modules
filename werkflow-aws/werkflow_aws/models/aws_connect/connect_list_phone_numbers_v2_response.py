from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_list_phone_numbers_summary import ConnectListPhoneNumbersSummary


class ConnectListPhoneNumbersV2Response(BaseModel):
    NextToken: StrictStr | None = None
    ListPhoneNumbersSummaryList: list[ConnectListPhoneNumbersSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
