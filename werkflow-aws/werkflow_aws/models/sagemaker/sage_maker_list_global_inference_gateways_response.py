from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_global_inference_gateway_summary import SageMakerGlobalInferenceGatewaySummary


class SageMakerListGlobalInferenceGatewaysResponse(BaseModel):
    GlobalInferenceGatewaySummaries: list[SageMakerGlobalInferenceGatewaySummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
