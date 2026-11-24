from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_model_package_summary import SageMakerModelPackageSummary


class SageMakerListModelPackagesResponse(BaseModel):
    ModelPackageSummaryList: list[SageMakerModelPackageSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
