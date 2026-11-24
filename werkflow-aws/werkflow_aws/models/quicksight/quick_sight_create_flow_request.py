from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_permission import QuickSightPermission
from .quick_sight_sensitive_document import QuickSightSensitiveDocument


class QuickSightCreateFlowRequest(BaseModel):
    AwsAccountId: StrictStr
    Name: StrictStr
    FlowDefinition: QuickSightSensitiveDocument
    Description: StrictStr | None = None
    Permissions: list[QuickSightPermission] | None = None
    ClientToken: StrictStr | None = None
