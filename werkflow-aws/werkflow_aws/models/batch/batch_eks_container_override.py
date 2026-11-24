from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .batch_eks_container_environment_variable import BatchEksContainerEnvironmentVariable
from .batch_eks_container_resource_requirements import BatchEksContainerResourceRequirements


class BatchEksContainerOverride(BaseModel):
    name: StrictStr | None = None
    image: StrictStr | None = None
    command: list[StrictStr] | None = None
    args: list[StrictStr] | None = None
    env: list[BatchEksContainerEnvironmentVariable] | None = None
    resources: BatchEksContainerResourceRequirements | None = None
