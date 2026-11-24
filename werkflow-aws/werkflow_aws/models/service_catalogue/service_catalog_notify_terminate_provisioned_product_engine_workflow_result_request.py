from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ServiceCatalogNotifyTerminateProvisionedProductEngineWorkflowResultRequest(BaseModel):
    WorkflowToken: StrictStr
    RecordId: StrictStr
    Status: Literal['SUCCEEDED', 'FAILED']
    IdempotencyToken: StrictStr
    FailureReason: StrictStr | None = None
