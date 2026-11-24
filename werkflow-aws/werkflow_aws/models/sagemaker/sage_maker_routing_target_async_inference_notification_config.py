from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerRoutingTargetAsyncInferenceNotificationConfig(BaseModel):
    SuccessTopic: StrictStr | None = None
    ErrorTopic: StrictStr | None = None
