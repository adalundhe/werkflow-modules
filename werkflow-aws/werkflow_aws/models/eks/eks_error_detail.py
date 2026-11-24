from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_error_code import EKSErrorCode


class EKSErrorDetail(BaseModel):
    errorCode: EKSErrorCode | None = None
    errorMessage: StrictStr | None = None
    resourceIds: list[StrictStr] | None = None
