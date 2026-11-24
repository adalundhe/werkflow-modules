from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .state_policy_rule import StatePolicyRule


class StatePolicyDocument(BaseModel):
    id: StrictStr | None = None
    isDefault: StrictBool | None = None
    policyDescription: StrictStr | None = None
    policyName: StrictStr | None = None
    rulesByDomain: dict[StrictStr, list[StatePolicyRule]] | None = None
    version: StrictInt | None = None
