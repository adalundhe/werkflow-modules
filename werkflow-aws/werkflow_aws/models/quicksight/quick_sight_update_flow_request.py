from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_sensitive_document import QuickSightSensitiveDocument


class QuickSightUpdateFlowRequest(BaseModel):
    AwsAccountId: StrictStr
    FlowId: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    FlowDefinition: QuickSightSensitiveDocument | None = None
    ClientToken: StrictStr | None = None
