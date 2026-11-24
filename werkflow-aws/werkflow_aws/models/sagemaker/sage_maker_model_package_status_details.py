from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_model_package_status_item import SageMakerModelPackageStatusItem


class SageMakerModelPackageStatusDetails(BaseModel):
    ValidationStatuses: list[SageMakerModelPackageStatusItem] | None = None
    ImageScanStatuses: list[SageMakerModelPackageStatusItem] | None = None
