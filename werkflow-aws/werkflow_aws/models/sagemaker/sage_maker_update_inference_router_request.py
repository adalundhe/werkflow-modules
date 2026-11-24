from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_routing_target import SageMakerRoutingTarget


class SageMakerUpdateInferenceRouterRequest(BaseModel):
    InferenceRouterName: StrictStr
    RoutingTargets: list[SageMakerRoutingTarget]
