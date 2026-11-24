from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_s3_account_public_access_block_details import SecurityHubAwsS3AccountPublicAccessBlockDetails
from .security_hub_aws_s3_bucket_bucket_lifecycle_configuration_details import SecurityHubAwsS3BucketBucketLifecycleConfigurationDetails
from .security_hub_aws_s3_bucket_bucket_versioning_configuration import SecurityHubAwsS3BucketBucketVersioningConfiguration
from .security_hub_aws_s3_bucket_logging_configuration import SecurityHubAwsS3BucketLoggingConfiguration
from .security_hub_aws_s3_bucket_notification_configuration import SecurityHubAwsS3BucketNotificationConfiguration
from .security_hub_aws_s3_bucket_object_lock_configuration import SecurityHubAwsS3BucketObjectLockConfiguration
from .security_hub_aws_s3_bucket_server_side_encryption_configuration import SecurityHubAwsS3BucketServerSideEncryptionConfiguration
from .security_hub_aws_s3_bucket_website_configuration import SecurityHubAwsS3BucketWebsiteConfiguration


class SecurityHubAwsS3BucketDetails(BaseModel):
    OwnerId: StrictStr | None = None
    OwnerName: StrictStr | None = None
    OwnerAccountId: StrictStr | None = None
    CreatedAt: StrictStr | None = None
    ServerSideEncryptionConfiguration: SecurityHubAwsS3BucketServerSideEncryptionConfiguration | None = None
    BucketLifecycleConfiguration: SecurityHubAwsS3BucketBucketLifecycleConfigurationDetails | None = None
    PublicAccessBlockConfiguration: SecurityHubAwsS3AccountPublicAccessBlockDetails | None = None
    AccessControlList: StrictStr | None = None
    BucketLoggingConfiguration: SecurityHubAwsS3BucketLoggingConfiguration | None = None
    BucketWebsiteConfiguration: SecurityHubAwsS3BucketWebsiteConfiguration | None = None
    BucketNotificationConfiguration: SecurityHubAwsS3BucketNotificationConfiguration | None = None
    BucketVersioningConfiguration: SecurityHubAwsS3BucketBucketVersioningConfiguration | None = None
    ObjectLockConfiguration: SecurityHubAwsS3BucketObjectLockConfiguration | None = None
    Name: StrictStr | None = None
