from __future__ import annotations
from pydantic import BaseModel
from .awss3_condition import AWSS3Condition
from .awss3_redirect import AWSS3Redirect


class AWSS3RoutingRule(BaseModel):
    Condition: AWSS3Condition | None = None
    Redirect: AWSS3Redirect | None = None
