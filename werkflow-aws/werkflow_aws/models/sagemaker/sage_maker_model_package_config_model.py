from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerModelPackageConfigModel(BaseModel):
    ModelPackageGroupArn: StrictStr | None = None
    SourceModelPackageArn: StrictStr | None = None
