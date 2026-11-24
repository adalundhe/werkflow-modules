from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudTrailUpdateTrailRequest(BaseModel):
    Name: StrictStr
    S3BucketName: StrictStr | None = None
    S3KeyPrefix: StrictStr | None = None
    SnsTopicName: StrictStr | None = None
    IncludeGlobalServiceEvents: StrictBool | None = None
    IsMultiRegionTrail: StrictBool | None = None
    EnableLogFileValidation: StrictBool | None = None
    CloudWatchLogsLogGroupArn: StrictStr | None = None
    CloudWatchLogsRoleArn: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    IsOrganizationTrail: StrictBool | None = None
    RecursiveLogging: StrictBool | None = None
