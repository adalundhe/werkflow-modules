from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .athena_named_query_model import AthenaNamedQueryModel
from .athena_unprocessed_named_query_id import AthenaUnprocessedNamedQueryId


class AthenaBatchGetNamedQueryResponse(BaseModel):
    NamedQueries: list[AthenaNamedQueryModel] | None = None
    UnprocessedNamedQueryIds: list[AthenaUnprocessedNamedQueryId] | None = None
    ResponseMetadata: dict[str, Any] | None = None
