from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2RuleGroupTypePair(BaseModel):
    RuleGroupArn: StrictStr | None = None
    RuleGroupType: StrictStr | None = None
