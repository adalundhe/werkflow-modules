from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt
from .batch_eks_seccomp_profile import BatchEksSeccompProfile


class BatchEksPodSecurityContext(BaseModel):
    runAsUser: StrictInt | None = None
    runAsGroup: StrictInt | None = None
    runAsNonRoot: StrictBool | None = None
    seccompProfile: BatchEksSeccompProfile | None = None
    fsGroup: StrictInt | None = None
