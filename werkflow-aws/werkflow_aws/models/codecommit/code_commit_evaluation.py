from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CodeCommitEvaluation(BaseModel):
    approved: StrictBool | None = None
    overridden: StrictBool | None = None
    approvalRulesSatisfied: list[StrictStr] | None = None
    approvalRulesNotSatisfied: list[StrictStr] | None = None
