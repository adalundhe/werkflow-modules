from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .athena_query_execution_model import AthenaQueryExecutionModel
from .athena_unprocessed_query_execution_id import AthenaUnprocessedQueryExecutionId


class AthenaBatchGetQueryExecutionResponse(BaseModel):
    QueryExecutions: list[AthenaQueryExecutionModel] | None = None
    UnprocessedQueryExecutionIds: list[AthenaUnprocessedQueryExecutionId] | None = None
    ResponseMetadata: dict[str, Any] | None = None
