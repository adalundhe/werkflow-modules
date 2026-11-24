from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_s3_bucket_object_lock_configuration_rule_details import SecurityHubAwsS3BucketObjectLockConfigurationRuleDetails


class SecurityHubAwsS3BucketObjectLockConfiguration(BaseModel):
    ObjectLockEnabled: StrictStr | None = None
    Rule: SecurityHubAwsS3BucketObjectLockConfigurationRuleDetails | None = None
