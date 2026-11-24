from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_client_stat import EKSClientStat


class EKSDeprecationDetail(BaseModel):
    usage: StrictStr | None = None
    replacedWith: StrictStr | None = None
    stopServingVersion: StrictStr | None = None
    startServingReplacementVersion: StrictStr | None = None
    clientStats: list[EKSClientStat] | None = None
