from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .sage_maker_traffic_routing_config import SageMakerTrafficRoutingConfig


class SageMakerBlueGreenUpdatePolicy(BaseModel):
    TrafficRoutingConfiguration: SageMakerTrafficRoutingConfig | None = None
    TerminationWaitInSeconds: StrictInt | None = None
    MaximumExecutionTimeoutInSeconds: StrictInt | None = None
