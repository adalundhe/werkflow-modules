from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class SageMakerUpdateMlflowTrackingServerRequest(BaseModel):
    TrackingServerName: StrictStr
    ArtifactStoreUri: StrictStr | None = None
    TrackingServerSize: Literal['Small', 'Medium', 'Large'] | None = None
    AutomaticModelRegistration: StrictBool | None = None
    WeeklyMaintenanceWindowStart: StrictStr | None = None
    S3BucketOwnerAccountId: StrictStr | None = None
    S3BucketOwnerVerification: StrictBool | None = None
