from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class StepFunctionsStartSyncExecutionRequest(BaseModel):
    stateMachineArn: StrictStr
    name: StrictStr | None = None
    input: StrictStr | None = None
    traceHeader: StrictStr | None = None
    includedData: Literal['ALL_DATA', 'METADATA_ONLY'] | None = None
