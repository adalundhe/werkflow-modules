from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsCloudTrailTrailDetails(BaseModel):
    CloudWatchLogsLogGroupArn: StrictStr | None = None
    CloudWatchLogsRoleArn: StrictStr | None = None
    HasCustomEventSelectors: StrictBool | None = None
    HomeRegion: StrictStr | None = None
    IncludeGlobalServiceEvents: StrictBool | None = None
    IsMultiRegionTrail: StrictBool | None = None
    IsOrganizationTrail: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    LogFileValidationEnabled: StrictBool | None = None
    Name: StrictStr | None = None
    S3BucketName: StrictStr | None = None
    S3KeyPrefix: StrictStr | None = None
    SnsTopicArn: StrictStr | None = None
    SnsTopicName: StrictStr | None = None
    TrailArn: StrictStr | None = None
