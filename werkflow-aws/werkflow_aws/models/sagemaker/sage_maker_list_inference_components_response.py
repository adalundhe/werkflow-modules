from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_inference_component_summary import SageMakerInferenceComponentSummary


class SageMakerListInferenceComponentsResponse(BaseModel):
    InferenceComponents: list[SageMakerInferenceComponentSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
