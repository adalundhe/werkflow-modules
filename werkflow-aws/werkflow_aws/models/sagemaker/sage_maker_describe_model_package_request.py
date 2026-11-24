from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SageMakerDescribeModelPackageRequest(BaseModel):
    ModelPackageName: StrictStr
    IncludedData: Literal['AllData', 'MetadataOnly'] | None = None
