from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .fms_protocols_list_data_summary import FMSProtocolsListDataSummary


class FMSListProtocolsListsResponse(BaseModel):
    ProtocolsLists: list[FMSProtocolsListDataSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
