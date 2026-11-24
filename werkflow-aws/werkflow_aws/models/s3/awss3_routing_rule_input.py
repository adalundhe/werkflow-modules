from __future__ import annotations
from pydantic import BaseModel
from .awss3_condition_input import AWSS3ConditionInput
from .awss3_redirect_input import AWSS3RedirectInput


class AWSS3RoutingRuleInput(BaseModel):
    Redirect: AWSS3RedirectInput
    Condition: AWSS3ConditionInput | None = None
