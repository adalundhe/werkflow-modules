from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_record_primary_value import ConnectRecordPrimaryValue


class ConnectListDataTablePrimaryValuesResponse(BaseModel):
    NextToken: StrictStr | None = None
    PrimaryValuesList: list[ConnectRecordPrimaryValue] | None = None
    ResponseMetadata: dict[str, Any] | None = None
