from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2SecurityGroupRuleDescription(BaseModel):
    SecurityGroupRuleId: StrictStr | None = None
    Description: StrictStr | None = None
