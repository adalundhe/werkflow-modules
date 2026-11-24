from __future__ import annotations
from pydantic import BaseModel
from .security_hub_aws_s3_bucket_server_side_encryption_rule import SecurityHubAwsS3BucketServerSideEncryptionRule


class SecurityHubAwsS3BucketServerSideEncryptionConfiguration(BaseModel):
    Rules: list[SecurityHubAwsS3BucketServerSideEncryptionRule] | None = None
