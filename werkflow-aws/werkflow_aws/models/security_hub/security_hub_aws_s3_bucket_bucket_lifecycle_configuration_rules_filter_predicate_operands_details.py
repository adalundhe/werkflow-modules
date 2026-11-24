from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_operands_tag_details import SecurityHubAwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetails


class SecurityHubAwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetails(BaseModel):
    Prefix: StrictStr | None = None
    Tag: SecurityHubAwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetails | None = None
    Type: StrictStr | None = None
