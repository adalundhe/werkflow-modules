from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_data_table_evaluated_value import ConnectDataTableEvaluatedValue


class ConnectEvaluateDataTableValuesResponse(BaseModel):
    Values: list[ConnectDataTableEvaluatedValue] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
