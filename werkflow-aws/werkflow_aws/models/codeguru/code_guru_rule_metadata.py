from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeGuruRuleMetadata(BaseModel):
    RuleId: StrictStr | None = None
    RuleName: StrictStr | None = None
    ShortDescription: StrictStr | None = None
    LongDescription: StrictStr | None = None
    RuleTags: list[StrictStr] | None = None
