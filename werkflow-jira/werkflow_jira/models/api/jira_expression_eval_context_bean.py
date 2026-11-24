from __future__ import annotations
from typing import TYPE_CHECKING
from pydantic import BaseModel, StrictInt
from .id_or_key_bean import IdOrKeyBean
from .jexp_issues import JexpIssues

if TYPE_CHECKING:
    from .custom_context_variable import CustomContextVariable


class JiraExpressionEvalContextBean(BaseModel):
    board: StrictInt | None = None
    custom: list[CustomContextVariable] | None = None
    customerRequest: StrictInt | None = None
    issue: IdOrKeyBean | None = None
    issues: JexpIssues | None = None
    project: IdOrKeyBean | None = None
    serviceDesk: StrictInt | None = None
    sprint: StrictInt | None = None
