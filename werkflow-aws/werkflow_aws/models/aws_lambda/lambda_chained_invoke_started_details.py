from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_event_input import LambdaEventInput


class LambdaChainedInvokeStartedDetails(BaseModel):
    FunctionName: StrictStr | None = None
    TenantId: StrictStr | None = None
    Input: LambdaEventInput | None = None
    ExecutedVersion: StrictStr | None = None
    DurableExecutionArn: StrictStr | None = None
