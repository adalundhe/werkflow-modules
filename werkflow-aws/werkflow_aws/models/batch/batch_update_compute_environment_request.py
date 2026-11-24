from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .batch_compute_resource_update import BatchComputeResourceUpdate
from .batch_ecs_settings import BatchEcsSettings
from .batch_eks_configuration_update import BatchEksConfigurationUpdate
from .batch_update_policy import BatchUpdatePolicy


class BatchUpdateComputeEnvironmentRequest(BaseModel):
    computeEnvironment: StrictStr
    state: Literal['ENABLED', 'DISABLED'] | None = None
    unmanagedvCpus: StrictInt | None = None
    computeResources: BatchComputeResourceUpdate | None = None
    serviceRole: StrictStr | None = None
    updatePolicy: BatchUpdatePolicy | None = None
    context: StrictStr | None = None
    ecsSettings: BatchEcsSettings | None = None
    eksConfiguration: BatchEksConfigurationUpdate | None = None
