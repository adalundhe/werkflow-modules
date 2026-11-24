from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .sage_maker_inference_component_placement_status import SageMakerInferenceComponentPlacementStatus


class SageMakerInferenceComponentRuntimeConfigSummary(BaseModel):
    DesiredCopyCount: StrictInt | None = None
    CurrentCopyCount: StrictInt | None = None
    PlacementStatus: list[SageMakerInferenceComponentPlacementStatus] | None = None
