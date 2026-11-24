from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .sage_maker_placement_specification import SageMakerPlacementSpecification


class SageMakerInstancePlacementConfig(BaseModel):
    EnableMultipleJobs: StrictBool | None = None
    PlacementSpecifications: list[SageMakerPlacementSpecification] | None = None
