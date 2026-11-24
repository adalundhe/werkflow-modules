from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SESGetReputationEntityRequest(BaseModel):
    ReputationEntityReference: StrictStr
    ReputationEntityType: Literal['RESOURCE']
