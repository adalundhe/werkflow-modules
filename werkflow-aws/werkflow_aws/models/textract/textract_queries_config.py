from __future__ import annotations
from pydantic import BaseModel
from .textract_query import TextractQuery


class TextractQueriesConfig(BaseModel):
    Queries: list[TextractQuery]
