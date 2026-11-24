from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_model_package_group_summary import SageMakerModelPackageGroupSummary


class SageMakerListModelPackageGroupsResponse(BaseModel):
    ModelPackageGroupSummaryList: list[SageMakerModelPackageGroupSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
