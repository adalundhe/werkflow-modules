from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_managed_configuration import SageMakerManagedConfiguration


class SageMakerModelPackageGroupSummary(BaseModel):
    ModelPackageGroupName: StrictStr | None = None
    ModelPackageGroupArn: StrictStr | None = None
    ModelPackageGroupDescription: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ModelPackageGroupStatus: StrictStr | None = None
    ManagedConfiguration: SageMakerManagedConfiguration | None = None
