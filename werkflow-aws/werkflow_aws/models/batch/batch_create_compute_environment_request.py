from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .batch_compute_resource import BatchComputeResource
from .batch_ecs_settings import BatchEcsSettings
from .batch_eks_configuration import BatchEksConfiguration


class BatchCreateComputeEnvironmentRequest(BaseModel):
    computeEnvironmentName: StrictStr
    type: Literal['MANAGED', 'UNMANAGED']
    state: Literal['ENABLED', 'DISABLED'] | None = None
    unmanagedvCpus: StrictInt | None = None
    computeResources: BatchComputeResource | None = None
    serviceRole: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    eksConfiguration: BatchEksConfiguration | None = None
    context: StrictStr | None = None
    ecsSettings: BatchEcsSettings | None = None
