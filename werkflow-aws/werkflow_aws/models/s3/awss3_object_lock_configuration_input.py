from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .awss3_object_lock_rule_input import AWSS3ObjectLockRuleInput


class AWSS3ObjectLockConfigurationInput(BaseModel):
    ObjectLockEnabled: Literal['Enabled'] | None = None
    Rule: AWSS3ObjectLockRuleInput | None = None
