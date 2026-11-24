from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_data_table_summary import ConnectDataTableSummary


class ConnectListDataTablesResponse(BaseModel):
    NextToken: StrictStr | None = None
    DataTableSummaryList: list[ConnectDataTableSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
