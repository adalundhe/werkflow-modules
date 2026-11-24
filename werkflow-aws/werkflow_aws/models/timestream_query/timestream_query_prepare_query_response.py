from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .timestream_query_parameter_mapping import TimestreamQueryParameterMapping
from .timestream_query_select_column import TimestreamQuerySelectColumn


class TimestreamQueryPrepareQueryResponse(BaseModel):
    QueryString: StrictStr | None = None
    Columns: list[TimestreamQuerySelectColumn] | None = None
    Parameters: list[TimestreamQueryParameterMapping] | None = None
    ResponseMetadata: dict[str, Any] | None = None
