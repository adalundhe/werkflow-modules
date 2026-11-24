from __future__ import annotations
from pydantic import BaseModel
from .awss3_lifecycle_rule_input import AWSS3LifecycleRuleInput


class AWSS3BucketLifecycleConfiguration(BaseModel):
    Rules: list[AWSS3LifecycleRuleInput]
