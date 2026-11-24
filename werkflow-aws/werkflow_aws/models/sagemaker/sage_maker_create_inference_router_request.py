from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_routing_target import SageMakerRoutingTarget
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateInferenceRouterRequest(BaseModel):
    InferenceRouterName: StrictStr
    RoutingTargets: list[SageMakerRoutingTarget]
    ClientToken: StrictStr | None = None
    Tags: list[SageMakerTagModel] | None = None
