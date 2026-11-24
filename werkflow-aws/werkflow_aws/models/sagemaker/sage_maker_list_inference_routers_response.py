from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_inference_router_summary import SageMakerInferenceRouterSummary


class SageMakerListInferenceRoutersResponse(BaseModel):
    InferenceRouters: list[SageMakerInferenceRouterSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
