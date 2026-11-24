from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .eks_cancellation import EKSCancellation
from .eks_error_detail import EKSErrorDetail
from .eks_update_param import EKSUpdateParam
from .eks_update_status import EKSUpdateStatus
from .eks_update_type import EKSUpdateType


class EKSUpdate(BaseModel):
    id: StrictStr | None = None
    status: EKSUpdateStatus | None = None
    type: EKSUpdateType | None = None
    params: list[EKSUpdateParam] | None = None
    createdAt: datetime.datetime | None = None
    errors: list[EKSErrorDetail] | None = None
    cancellation: EKSCancellation | None = None
