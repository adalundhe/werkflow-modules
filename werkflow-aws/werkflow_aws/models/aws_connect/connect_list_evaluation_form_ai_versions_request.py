from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListEvaluationFormAIVersionsRequest(BaseModel):
    InstanceId: StrictStr
    ContactInteractionType: Literal['AGENT', 'AUTOMATED', 'CUSTOMER']
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
