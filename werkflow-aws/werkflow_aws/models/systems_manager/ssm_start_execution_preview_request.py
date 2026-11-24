from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ssm_execution_inputs import SSMExecutionInputs


class SSMStartExecutionPreviewRequest(BaseModel):
    DocumentName: StrictStr
    DocumentVersion: StrictStr | None = None
    ExecutionInputs: SSMExecutionInputs | None = None
