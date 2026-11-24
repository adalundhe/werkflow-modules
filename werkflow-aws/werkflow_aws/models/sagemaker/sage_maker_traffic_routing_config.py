from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .sage_maker_capacity_size import SageMakerCapacitySize
from .sage_maker_traffic_routing_config_type import SageMakerTrafficRoutingConfigType


class SageMakerTrafficRoutingConfig(BaseModel):
    Type: SageMakerTrafficRoutingConfigType | None = None
    WaitIntervalInSeconds: StrictInt | None = None
    CanarySize: SageMakerCapacitySize | None = None
    LinearStepSize: SageMakerCapacitySize | None = None
