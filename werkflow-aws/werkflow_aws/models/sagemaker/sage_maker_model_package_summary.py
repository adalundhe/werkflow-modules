from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_model_life_cycle import SageMakerModelLifeCycle


class SageMakerModelPackageSummary(BaseModel):
    ModelPackageName: StrictStr | None = None
    ModelPackageGroupName: StrictStr | None = None
    ModelPackageVersion: StrictInt | None = None
    ModelPackageArn: StrictStr | None = None
    ModelPackageDescription: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ModelPackageStatus: StrictStr | None = None
    ModelApprovalStatus: StrictStr | None = None
    ModelLifeCycle: SageMakerModelLifeCycle | None = None
    ModelPackageRegistrationType: StrictStr | None = None
