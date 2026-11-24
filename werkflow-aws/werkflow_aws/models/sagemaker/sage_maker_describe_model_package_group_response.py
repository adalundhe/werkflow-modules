from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_managed_configuration import SageMakerManagedConfiguration
from .sage_maker_user_context_model import SageMakerUserContextModel


class SageMakerDescribeModelPackageGroupResponse(BaseModel):
    ModelPackageGroupName: StrictStr | None = None
    ModelPackageGroupArn: StrictStr | None = None
    ModelPackageGroupDescription: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    CreatedBy: SageMakerUserContextModel | None = None
    ModelPackageGroupStatus: StrictStr | None = None
    ManagedConfiguration: SageMakerManagedConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
