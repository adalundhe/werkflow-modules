from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectCreateUseCaseRequest(BaseModel):
    InstanceId: StrictStr
    IntegrationAssociationId: StrictStr
    UseCaseType: Literal['RULES_EVALUATION', 'CONNECT_CAMPAIGNS']
    Tags: dict[StrictStr, StrictStr] | None = None
