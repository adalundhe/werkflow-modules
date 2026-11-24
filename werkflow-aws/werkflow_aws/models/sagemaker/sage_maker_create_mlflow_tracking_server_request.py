from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateMlflowTrackingServerRequest(BaseModel):
    TrackingServerName: StrictStr
    ArtifactStoreUri: StrictStr
    RoleArn: StrictStr
    TrackingServerSize: Literal['Small', 'Medium', 'Large'] | None = None
    MlflowVersion: StrictStr | None = None
    AutomaticModelRegistration: StrictBool | None = None
    WeeklyMaintenanceWindowStart: StrictStr | None = None
    Tags: list[SageMakerTagModel] | None = None
    S3BucketOwnerAccountId: StrictStr | None = None
    S3BucketOwnerVerification: StrictBool | None = None
