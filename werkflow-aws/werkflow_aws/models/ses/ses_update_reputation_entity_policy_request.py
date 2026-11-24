from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SESUpdateReputationEntityPolicyRequest(BaseModel):
    ReputationEntityType: Literal['RESOURCE']
    ReputationEntityReference: StrictStr
    ReputationEntityPolicy: StrictStr
