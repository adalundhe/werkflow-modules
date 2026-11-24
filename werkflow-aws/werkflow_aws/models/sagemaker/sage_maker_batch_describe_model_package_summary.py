from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_inference_specification import SageMakerInferenceSpecification


class SageMakerBatchDescribeModelPackageSummary(BaseModel):
    ModelPackageGroupName: StrictStr | None = None
    ModelPackageVersion: StrictInt | None = None
    ModelPackageArn: StrictStr | None = None
    ModelPackageDescription: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    InferenceSpecification: SageMakerInferenceSpecification | None = None
    ModelPackageStatus: StrictStr | None = None
    ModelApprovalStatus: StrictStr | None = None
    ModelPackageRegistrationType: StrictStr | None = None
