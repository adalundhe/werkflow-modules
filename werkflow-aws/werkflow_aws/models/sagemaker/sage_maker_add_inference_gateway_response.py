from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_global_inference_gateway_member import SageMakerGlobalInferenceGatewayMember


class SageMakerAddInferenceGatewayResponse(BaseModel):
    Arn: StrictStr | None = None
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Gateway: SageMakerGlobalInferenceGatewayMember | None = None
    Status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
