from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSHorizontalPodAutoscalerControllerConfigRequest(BaseModel):
    horizontalPodAutoscalerSyncPeriod: StrictStr | None = None
