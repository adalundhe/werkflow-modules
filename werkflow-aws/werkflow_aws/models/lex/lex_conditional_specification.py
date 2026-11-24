from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .lex_conditional_branch import LexConditionalBranch
from .lex_default_conditional_branch import LexDefaultConditionalBranch


class LexConditionalSpecification(BaseModel):
    active: StrictBool | None = None
    conditionalBranches: list[LexConditionalBranch] | None = None
    defaultBranch: LexDefaultConditionalBranch | None = None
