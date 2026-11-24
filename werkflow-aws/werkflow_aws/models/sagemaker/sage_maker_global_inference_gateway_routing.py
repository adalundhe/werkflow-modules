from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_global_inference_gateway_routing_weights import SageMakerGlobalInferenceGatewayRoutingWeights


class SageMakerGlobalInferenceGatewayRouting(BaseModel):
    Weights: SageMakerGlobalInferenceGatewayRoutingWeights | None = None
