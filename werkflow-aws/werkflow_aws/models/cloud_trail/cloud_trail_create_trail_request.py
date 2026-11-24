from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_trail_tag import CloudTrailTag


class CloudTrailCreateTrailRequest(BaseModel):
    Name: StrictStr
    S3BucketName: StrictStr
    S3KeyPrefix: StrictStr | None = None
    SnsTopicName: StrictStr | None = None
    IncludeGlobalServiceEvents: StrictBool | None = None
    IsMultiRegionTrail: StrictBool | None = None
    EnableLogFileValidation: StrictBool | None = None
    CloudWatchLogsLogGroupArn: StrictStr | None = None
    CloudWatchLogsRoleArn: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    IsOrganizationTrail: StrictBool | None = None
    TagsList: list[CloudTrailTag] | None = None
    RecursiveLogging: StrictBool | None = None
