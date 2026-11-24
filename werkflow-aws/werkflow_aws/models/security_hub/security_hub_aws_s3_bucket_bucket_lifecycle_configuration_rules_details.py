from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_aws_s3_bucket_bucket_lifecycle_configuration_rules_abort_incomplete_multipart_upload_details import SecurityHubAwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetails
from .security_hub_aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_details import SecurityHubAwsS3BucketBucketLifecycleConfigurationRulesFilterDetails
from .security_hub_aws_s3_bucket_bucket_lifecycle_configuration_rules_noncurrent_version_transitions_details import SecurityHubAwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetails
from .security_hub_aws_s3_bucket_bucket_lifecycle_configuration_rules_transitions_details import SecurityHubAwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetails


class SecurityHubAwsS3BucketBucketLifecycleConfigurationRulesDetails(BaseModel):
    AbortIncompleteMultipartUpload: SecurityHubAwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetails | None = None
    ExpirationDate: StrictStr | None = None
    ExpirationInDays: StrictInt | None = None
    ExpiredObjectDeleteMarker: StrictBool | None = None
    Filter: SecurityHubAwsS3BucketBucketLifecycleConfigurationRulesFilterDetails | None = None
    ID: StrictStr | None = None
    NoncurrentVersionExpirationInDays: StrictInt | None = None
    NoncurrentVersionTransitions: list[SecurityHubAwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetails] | None = None
    Prefix: StrictStr | None = None
    Status: StrictStr | None = None
    Transitions: list[SecurityHubAwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetails] | None = None
