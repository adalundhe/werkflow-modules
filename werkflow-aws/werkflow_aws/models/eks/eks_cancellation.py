from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_cancellation_status import EKSCancellationStatus


class EKSCancellation(BaseModel):
    status: EKSCancellationStatus | None = None
    reason: StrictStr | None = None
