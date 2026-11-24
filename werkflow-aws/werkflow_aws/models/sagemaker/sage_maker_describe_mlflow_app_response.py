from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_user_context_model import SageMakerUserContextModel


class SageMakerDescribeMlflowAppResponse(BaseModel):
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    ArtifactStoreUri: StrictStr | None = None
    MlflowVersion: StrictStr | None = None
    RoleArn: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    Status: StrictStr | None = None
    ModelRegistrationMode: StrictStr | None = None
    AccountDefaultStatus: StrictStr | None = None
    DefaultDomainIdList: list[StrictStr] | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    CreatedBy: SageMakerUserContextModel | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedBy: SageMakerUserContextModel | None = None
    WeeklyMaintenanceWindowStart: StrictStr | None = None
    MaintenanceStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
