from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_global_inference_gateway_member_summary import SageMakerGlobalInferenceGatewayMemberSummary


class SageMakerListInferenceGatewaysResponse(BaseModel):
    InferenceGatewaySummaries: list[SageMakerGlobalInferenceGatewayMemberSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
