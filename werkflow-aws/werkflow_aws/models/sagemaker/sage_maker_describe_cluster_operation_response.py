from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_cluster_operation_scaling_details import SageMakerClusterOperationScalingDetails
from .sage_maker_instance_group_health_check_configuration import SageMakerInstanceGroupHealthCheckConfiguration


class SageMakerDescribeClusterOperationResponse(BaseModel):
    OperationId: StrictStr | None = None
    ClusterArn: StrictStr | None = None
    Type: StrictStr | None = None
    Status: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ScalingDetails: list[SageMakerClusterOperationScalingDetails] | None = None
    DeepHealthCheckDetails: list[SageMakerInstanceGroupHealthCheckConfiguration] | None = None
    ResponseMetadata: dict[str, Any] | None = None
