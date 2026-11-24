from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_batch_describe_model_package_error import SageMakerBatchDescribeModelPackageError
from .sage_maker_batch_describe_model_package_summary import SageMakerBatchDescribeModelPackageSummary


class SageMakerBatchDescribeModelPackageResponse(BaseModel):
    ModelPackageSummaries: dict[StrictStr, SageMakerBatchDescribeModelPackageSummary] | None = None
    BatchDescribeModelPackageErrorMap: dict[StrictStr, SageMakerBatchDescribeModelPackageError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
