from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .sage_maker_placement_specification_model import SageMakerPlacementSpecificationModel


class SageMakerInstancePlacementConfigModel(BaseModel):
    EnableMultipleJobs: StrictBool | None = None
    PlacementSpecifications: list[SageMakerPlacementSpecificationModel] | None = None
