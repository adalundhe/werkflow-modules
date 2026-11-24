from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_model_package_validation_profile import SageMakerModelPackageValidationProfile


class SageMakerModelPackageValidationSpecification(BaseModel):
    ValidationRole: StrictStr | None = None
    ValidationProfiles: list[SageMakerModelPackageValidationProfile] | None = None
