from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_statement_output_data import GlueStatementOutputData


class GlueStatementOutput(BaseModel):
    Data: GlueStatementOutputData | None = None
    ExecutionCount: StrictInt | None = None
    Status: StrictStr | None = None
    ErrorName: StrictStr | None = None
    ErrorValue: StrictStr | None = None
    Traceback: list[StrictStr] | None = None
