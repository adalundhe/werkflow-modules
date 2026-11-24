from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .jql_query import JqlQuery


class ParsedJqlQuery(BaseModel):
    errors: list[StrictStr] | None = None
    query: StrictStr | None = None
    structure: JqlQuery | None = None
    warnings: list[StrictStr] | None = None
