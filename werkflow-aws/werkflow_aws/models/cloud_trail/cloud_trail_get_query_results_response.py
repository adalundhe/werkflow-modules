from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_trail_query_statistics import CloudTrailQueryStatistics


class CloudTrailGetQueryResultsResponse(BaseModel):
    QueryStatus: StrictStr | None = None
    QueryStatistics: CloudTrailQueryStatistics | None = None
    QueryResultRows: list[list[dict[StrictStr, StrictStr]]] | None = None
    NextToken: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
