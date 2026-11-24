from __future__ import annotations
from typing import TYPE_CHECKING
from pydantic import BaseModel, StrictInt
from .id_or_key_bean import IdOrKeyBean
from .jexp_evaluate_ctx_issues import JexpEvaluateCtxIssues

if TYPE_CHECKING:
    from .custom_context_variable import CustomContextVariable


class JiraExpressionEvaluateContextBean(BaseModel):
    board: StrictInt | None = None
    custom: list[CustomContextVariable] | None = None
    customerRequest: StrictInt | None = None
    issue: IdOrKeyBean | None = None
    issues: JexpEvaluateCtxIssues | None = None
    project: IdOrKeyBean | None = None
    serviceDesk: StrictInt | None = None
    sprint: StrictInt | None = None
