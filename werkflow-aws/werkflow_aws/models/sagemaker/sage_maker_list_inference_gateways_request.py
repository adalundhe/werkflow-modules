from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_global_inference_gateway_member_filter import SageMakerGlobalInferenceGatewayMemberFilter


class SageMakerListInferenceGatewaysRequest(BaseModel):
    Identifier: StrictStr
    Filters: list[SageMakerGlobalInferenceGatewayMemberFilter] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
