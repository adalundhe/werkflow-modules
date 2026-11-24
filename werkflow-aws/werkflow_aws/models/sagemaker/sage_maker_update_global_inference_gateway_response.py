from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_global_inference_gateway_routing import SageMakerGlobalInferenceGatewayRouting


class SageMakerUpdateGlobalInferenceGatewayResponse(BaseModel):
    Arn: StrictStr | None = None
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    Routing: SageMakerGlobalInferenceGatewayRouting | None = None
    ResponseMetadata: dict[str, Any] | None = None
