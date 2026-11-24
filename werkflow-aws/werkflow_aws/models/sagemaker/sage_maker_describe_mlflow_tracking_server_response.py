from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_user_context_model import SageMakerUserContextModel


class SageMakerDescribeMlflowTrackingServerResponse(BaseModel):
    TrackingServerArn: StrictStr | None = None
    TrackingServerName: StrictStr | None = None
    ArtifactStoreUri: StrictStr | None = None
    TrackingServerSize: StrictStr | None = None
    MlflowVersion: StrictStr | None = None
    RoleArn: StrictStr | None = None
    TrackingServerStatus: StrictStr | None = None
    TrackingServerMaintenanceStatus: StrictStr | None = None
    IsActive: StrictStr | None = None
    TrackingServerUrl: StrictStr | None = None
    WeeklyMaintenanceWindowStart: StrictStr | None = None
    AutomaticModelRegistration: StrictBool | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    CreatedBy: SageMakerUserContextModel | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedBy: SageMakerUserContextModel | None = None
    S3BucketOwnerAccountId: StrictStr | None = None
    S3BucketOwnerVerification: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
