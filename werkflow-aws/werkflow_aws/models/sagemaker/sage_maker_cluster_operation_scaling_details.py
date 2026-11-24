from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_cluster_operation_scaling_configuration import SageMakerClusterOperationScalingConfiguration


class SageMakerClusterOperationScalingDetails(BaseModel):
    InstanceGroupName: StrictStr | None = None
    Status: StrictStr | None = None
    Original: SageMakerClusterOperationScalingConfiguration | None = None
    Desired: SageMakerClusterOperationScalingConfiguration | None = None
