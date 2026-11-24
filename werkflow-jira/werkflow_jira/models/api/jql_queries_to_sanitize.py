from __future__ import annotations
from pydantic import BaseModel
from .jql_query_to_sanitize import JqlQueryToSanitize


class JqlQueriesToSanitize(BaseModel):
    queries: list[JqlQueryToSanitize] | None = None
