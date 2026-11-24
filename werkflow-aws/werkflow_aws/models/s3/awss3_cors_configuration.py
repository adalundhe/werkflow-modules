from __future__ import annotations
from pydantic import BaseModel
from .awss3_cors_rule_input import AWSS3CORSRuleInput


class AWSS3CORSConfiguration(BaseModel):
    CORSRules: list[AWSS3CORSRuleInput]
