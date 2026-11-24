from __future__ import annotations
from pydantic import BaseModel
from .sanitized_jql_query import SanitizedJqlQuery


class SanitizedJqlQueries(BaseModel):
    queries: list[SanitizedJqlQuery] | None = None
