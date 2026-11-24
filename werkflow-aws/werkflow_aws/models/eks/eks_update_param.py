from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_update_param_type import EKSUpdateParamType


class EKSUpdateParam(BaseModel):
    type: EKSUpdateParamType | None = None
    value: StrictStr | None = None
