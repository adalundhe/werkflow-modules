from __future__ import annotations
from pydantic import BaseModel
from .parsed_jql_query import ParsedJqlQuery


class ParsedJqlQueries(BaseModel):
    queries: list[ParsedJqlQuery] | None = None
