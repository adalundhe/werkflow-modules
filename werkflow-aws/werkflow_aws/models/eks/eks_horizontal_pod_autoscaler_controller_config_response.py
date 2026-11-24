from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSHorizontalPodAutoscalerControllerConfigResponse(BaseModel):
    horizontalPodAutoscalerSyncPeriod: StrictStr | None = None
