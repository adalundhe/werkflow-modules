from __future__ import annotations
from pydantic import BaseModel
from .jexp_jql_issues import JexpJqlIssues


class JexpIssues(BaseModel):
    jql: JexpJqlIssues | None = None
