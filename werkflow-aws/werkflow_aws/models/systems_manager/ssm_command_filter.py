from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SSMCommandFilter(BaseModel):
    key: Literal['InvokedAfter', 'InvokedBefore', 'Status', 'ExecutionStage', 'DocumentName']
    value: StrictStr
