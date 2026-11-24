from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsRedshiftClusterLoggingStatus(BaseModel):
    BucketName: StrictStr | None = None
    LastFailureMessage: StrictStr | None = None
    LastFailureTime: StrictStr | None = None
    LastSuccessfulDeliveryTime: StrictStr | None = None
    LoggingEnabled: StrictBool | None = None
    S3KeyPrefix: StrictStr | None = None
