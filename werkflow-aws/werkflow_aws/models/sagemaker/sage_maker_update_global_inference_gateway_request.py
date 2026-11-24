from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_global_inference_gateway_routing import SageMakerGlobalInferenceGatewayRouting


class SageMakerUpdateGlobalInferenceGatewayRequest(BaseModel):
    Identifier: StrictStr
    Routing: SageMakerGlobalInferenceGatewayRouting
