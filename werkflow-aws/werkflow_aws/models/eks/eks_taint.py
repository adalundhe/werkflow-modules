from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_taint_effect import EKSTaintEffect


class EKSTaint(BaseModel):
    key: StrictStr | None = None
    value: StrictStr | None = None
    effect: EKSTaintEffect | None = None
