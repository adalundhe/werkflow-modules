from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class CloudTrailUpdateTrailResponse(BaseModel):
    Name: StrictStr | None = None
    S3BucketName: StrictStr | None = None
    S3KeyPrefix: StrictStr | None = None
    SnsTopicName: StrictStr | None = None
    SnsTopicARN: StrictStr | None = None
    IncludeGlobalServiceEvents: StrictBool | None = None
    IsMultiRegionTrail: StrictBool | None = None
    TrailARN: StrictStr | None = None
    LogFileValidationEnabled: StrictBool | None = None
    CloudWatchLogsLogGroupArn: StrictStr | None = None
    CloudWatchLogsRoleArn: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    IsOrganizationTrail: StrictBool | None = None
    RecursiveLogging: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
