from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_algorithm_status_item import SageMakerAlgorithmStatusItem


class SageMakerAlgorithmStatusDetails(BaseModel):
    ValidationStatuses: list[SageMakerAlgorithmStatusItem] | None = None
    ImageScanStatuses: list[SageMakerAlgorithmStatusItem] | None = None
