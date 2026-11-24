from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_contact_search_summary import ConnectContactSearchSummary


class ConnectSearchContactsResponse(BaseModel):
    Contacts: list[ConnectContactSearchSummary] | None = None
    NextToken: StrictStr | None = None
    TotalCount: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
