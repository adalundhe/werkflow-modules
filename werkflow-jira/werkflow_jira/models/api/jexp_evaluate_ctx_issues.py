from __future__ import annotations
from pydantic import BaseModel
from .jexp_evaluate_ctx_jql_issues import JexpEvaluateCtxJqlIssues


class JexpEvaluateCtxIssues(BaseModel):
    jql: JexpEvaluateCtxJqlIssues | None = None
