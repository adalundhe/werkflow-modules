from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .simple_error_collection import SimpleErrorCollection


class RemoveOptionFromIssuesResult(BaseModel):
    errors: SimpleErrorCollection | None = None
    modifiedIssues: list[StrictInt] | None = None
    unmodifiedIssues: list[StrictInt] | None = None
