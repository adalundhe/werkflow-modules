from __future__ import annotations
from pydantic import BaseModel
from .cognito_idp_failover_type import CognitoIDPFailoverType


class CognitoIDPRoutingType(BaseModel):
    Failover: CognitoIDPFailoverType | None = None
