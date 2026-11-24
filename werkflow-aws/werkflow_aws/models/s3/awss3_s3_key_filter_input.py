from __future__ import annotations
from pydantic import BaseModel
from .awss3_filter_rule_input import AWSS3FilterRuleInput


class AWSS3S3KeyFilterInput(BaseModel):
    FilterRules: list[AWSS3FilterRuleInput] | None = None
