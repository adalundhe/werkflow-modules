from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSHorizontalPodAutoscalerControllerConfigResponseModel(BaseModel):
    horizontalPodAutoscalerSyncPeriod: StrictStr | None = None
