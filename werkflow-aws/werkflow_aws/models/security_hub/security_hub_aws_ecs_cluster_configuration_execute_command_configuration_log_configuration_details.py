from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetails(BaseModel):
    CloudWatchEncryptionEnabled: StrictBool | None = None
    CloudWatchLogGroupName: StrictStr | None = None
    S3BucketName: StrictStr | None = None
    S3EncryptionEnabled: StrictBool | None = None
    S3KeyPrefix: StrictStr | None = None
