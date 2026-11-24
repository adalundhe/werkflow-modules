from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .glue_statement_output import GlueStatementOutput


class GlueStatement(BaseModel):
    Id: StrictInt | None = None
    Code: StrictStr | None = None
    State: StrictStr | None = None
    Output: GlueStatementOutput | None = None
    Progress: StrictFloat | StrictInt | None = None
    StartedOn: StrictInt | None = None
    CompletedOn: StrictInt | None = None
