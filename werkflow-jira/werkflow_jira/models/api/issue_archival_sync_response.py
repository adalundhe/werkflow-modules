from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .errors import Errors


class IssueArchivalSyncResponse(BaseModel):
    errors: Errors | None = None
    numberOfIssuesUpdated: StrictInt | None = None
