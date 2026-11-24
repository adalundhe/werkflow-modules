from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_data_table_value_summary import ConnectDataTableValueSummary


class ConnectListDataTableValuesResponse(BaseModel):
    NextToken: StrictStr | None = None
    Values: list[ConnectDataTableValueSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
