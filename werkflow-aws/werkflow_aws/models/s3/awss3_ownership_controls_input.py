from __future__ import annotations
from pydantic import BaseModel
from .awss3_ownership_controls_rule_input import AWSS3OwnershipControlsRuleInput


class AWSS3OwnershipControlsInput(BaseModel):
    Rules: list[AWSS3OwnershipControlsRuleInput]
