from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_global_inference_gateway_filter import SageMakerGlobalInferenceGatewayFilter


class SageMakerListGlobalInferenceGatewaysRequest(BaseModel):
    Filters: list[SageMakerGlobalInferenceGatewayFilter] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
