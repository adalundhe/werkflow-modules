from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerModelPackageConfig(BaseModel):
    ModelPackageGroupArn: StrictStr | None = None
    SourceModelPackageArn: StrictStr | None = None
