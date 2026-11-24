from __future__ import annotations
from pydantic import BaseModel
from .issue_matches_for_jql import IssueMatchesForJQL


class IssueMatches(BaseModel):
    matches: list[IssueMatchesForJQL] | None = None
