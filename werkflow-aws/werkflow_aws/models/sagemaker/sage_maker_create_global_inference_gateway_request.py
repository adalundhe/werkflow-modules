from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_global_inference_gateway_member import SageMakerGlobalInferenceGatewayMember
from .sage_maker_global_inference_gateway_routing import SageMakerGlobalInferenceGatewayRouting
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateGlobalInferenceGatewayRequest(BaseModel):
    Name: StrictStr
    ExecutionRoleArn: StrictStr
    Gateways: list[SageMakerGlobalInferenceGatewayMember]
    Routing: SageMakerGlobalInferenceGatewayRouting | None = None
    ClientToken: StrictStr | None = None
    Tags: list[SageMakerTagModel] | None = None
