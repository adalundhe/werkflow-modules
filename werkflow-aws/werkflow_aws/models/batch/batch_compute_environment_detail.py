from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .batch_compute_resource import BatchComputeResource
from .batch_ecs_settings import BatchEcsSettings
from .batch_eks_configuration import BatchEksConfiguration
from .batch_update_policy import BatchUpdatePolicy


class BatchComputeEnvironmentDetail(BaseModel):
    computeEnvironmentName: StrictStr | None = None
    computeEnvironmentArn: StrictStr | None = None
    unmanagedvCpus: StrictInt | None = None
    ecsClusterArn: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    type: StrictStr | None = None
    state: StrictStr | None = None
    status: StrictStr | None = None
    statusReason: StrictStr | None = None
    computeResources: BatchComputeResource | None = None
    serviceRole: StrictStr | None = None
    updatePolicy: BatchUpdatePolicy | None = None
    eksConfiguration: BatchEksConfiguration | None = None
    containerOrchestrationType: StrictStr | None = None
    uuid: StrictStr | None = None
    context: StrictStr | None = None
    ecsSettings: BatchEcsSettings | None = None
