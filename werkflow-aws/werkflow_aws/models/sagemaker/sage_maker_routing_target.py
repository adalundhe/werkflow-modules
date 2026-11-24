from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_destination import SageMakerDestination
from .sage_maker_routing_target_async_inference_config import SageMakerRoutingTargetAsyncInferenceConfig


class SageMakerRoutingTarget(BaseModel):
    Name: StrictStr | None = None
    Destinations: list[SageMakerDestination] | None = None
    AsyncInferenceConfig: SageMakerRoutingTargetAsyncInferenceConfig | None = None
    RoutingPreference: StrictStr | None = None
