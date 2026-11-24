from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferListedWorkflow(BaseModel):
    WorkflowId: StrictStr | None = None
    Description: StrictStr | None = None
    Arn: StrictStr | None = None
