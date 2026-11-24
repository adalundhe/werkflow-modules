from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerSendPipelineExecutionStepFailureRequest(BaseModel):
    CallbackToken: StrictStr
    FailureReason: StrictStr | None = None
    ClientRequestToken: StrictStr | None = None
