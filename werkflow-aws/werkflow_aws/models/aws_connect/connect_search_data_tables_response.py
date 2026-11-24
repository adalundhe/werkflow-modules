from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_data_table import ConnectDataTable


class ConnectSearchDataTablesResponse(BaseModel):
    DataTables: list[ConnectDataTable] | None = None
    NextToken: StrictStr | None = None
    ApproximateTotalCount: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
