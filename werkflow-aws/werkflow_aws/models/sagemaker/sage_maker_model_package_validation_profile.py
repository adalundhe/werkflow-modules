from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_transform_job_definition import SageMakerTransformJobDefinition


class SageMakerModelPackageValidationProfile(BaseModel):
    ProfileName: StrictStr | None = None
    TransformJobDefinition: SageMakerTransformJobDefinition | None = None
