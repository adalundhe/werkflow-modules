from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .athena_prepared_statement_model import AthenaPreparedStatementModel
from .athena_unprocessed_prepared_statement_name import AthenaUnprocessedPreparedStatementName


class AthenaBatchGetPreparedStatementResponse(BaseModel):
    PreparedStatements: list[AthenaPreparedStatementModel] | None = None
    UnprocessedPreparedStatementNames: list[AthenaUnprocessedPreparedStatementName] | None = None
    ResponseMetadata: dict[str, Any] | None = None
