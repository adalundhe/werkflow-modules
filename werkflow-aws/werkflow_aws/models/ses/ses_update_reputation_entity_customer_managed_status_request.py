from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SESUpdateReputationEntityCustomerManagedStatusRequest(BaseModel):
    ReputationEntityType: Literal['RESOURCE']
    ReputationEntityReference: StrictStr
    SendingStatus: Literal['ENABLED', 'REINSTATED', 'DISABLED']
