from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_instance_group_health_check_configuration import SageMakerInstanceGroupHealthCheckConfiguration


class SageMakerStartClusterHealthCheckRequest(BaseModel):
    ClusterName: StrictStr
    DeepHealthCheckConfigurations: list[SageMakerInstanceGroupHealthCheckConfiguration]
