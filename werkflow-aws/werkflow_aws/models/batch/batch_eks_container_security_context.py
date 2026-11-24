from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt
from .batch_eks_container_linux_capabilities import BatchEksContainerLinuxCapabilities
from .batch_eks_seccomp_profile import BatchEksSeccompProfile


class BatchEksContainerSecurityContext(BaseModel):
    runAsUser: StrictInt | None = None
    runAsGroup: StrictInt | None = None
    privileged: StrictBool | None = None
    allowPrivilegeEscalation: StrictBool | None = None
    readOnlyRootFilesystem: StrictBool | None = None
    runAsNonRoot: StrictBool | None = None
    capabilities: BatchEksContainerLinuxCapabilities | None = None
    seccompProfile: BatchEksSeccompProfile | None = None
