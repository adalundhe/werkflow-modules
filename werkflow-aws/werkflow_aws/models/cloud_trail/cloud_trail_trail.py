from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudTrailTrail(BaseModel):
    Name: StrictStr | None = None
    S3BucketName: StrictStr | None = None
    S3KeyPrefix: StrictStr | None = None
    SnsTopicName: StrictStr | None = None
    SnsTopicARN: StrictStr | None = None
    IncludeGlobalServiceEvents: StrictBool | None = None
    IsMultiRegionTrail: StrictBool | None = None
    HomeRegion: StrictStr | None = None
    TrailARN: StrictStr | None = None
    LogFileValidationEnabled: StrictBool | None = None
    CloudWatchLogsLogGroupArn: StrictStr | None = None
    CloudWatchLogsRoleArn: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    HasCustomEventSelectors: StrictBool | None = None
    HasInsightSelectors: StrictBool | None = None
    IsOrganizationTrail: StrictBool | None = None
    RecursiveLogging: StrictBool | None = None
