from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_algorithm_validation_profile import SageMakerAlgorithmValidationProfile


class SageMakerAlgorithmValidationSpecification(BaseModel):
    ValidationRole: StrictStr | None = None
    ValidationProfiles: list[SageMakerAlgorithmValidationProfile] | None = None
