from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .batch_eks_container_environment_variable import BatchEksContainerEnvironmentVariable
from .batch_eks_container_resource_requirements import BatchEksContainerResourceRequirements
from .batch_eks_container_security_context import BatchEksContainerSecurityContext
from .batch_eks_container_volume_mount import BatchEksContainerVolumeMount


class BatchEksContainerDetail(BaseModel):
    name: StrictStr | None = None
    image: StrictStr | None = None
    imagePullPolicy: StrictStr | None = None
    command: list[StrictStr] | None = None
    args: list[StrictStr] | None = None
    env: list[BatchEksContainerEnvironmentVariable] | None = None
    resources: BatchEksContainerResourceRequirements | None = None
    exitCode: StrictInt | None = None
    reason: StrictStr | None = None
    volumeMounts: list[BatchEksContainerVolumeMount] | None = None
    securityContext: BatchEksContainerSecurityContext | None = None
