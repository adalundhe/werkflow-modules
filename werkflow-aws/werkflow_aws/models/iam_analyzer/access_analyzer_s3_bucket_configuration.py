from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .access_analyzer_s3_access_point_configuration import AccessAnalyzerS3AccessPointConfiguration
from .access_analyzer_s3_bucket_acl_grant_configuration import AccessAnalyzerS3BucketAclGrantConfiguration
from .access_analyzer_s3_public_access_block_configuration import AccessAnalyzerS3PublicAccessBlockConfiguration


class AccessAnalyzerS3BucketConfiguration(BaseModel):
    bucketPolicy: StrictStr | None = None
    bucketAclGrants: list[AccessAnalyzerS3BucketAclGrantConfiguration] | None = None
    bucketPublicAccessBlock: AccessAnalyzerS3PublicAccessBlockConfiguration | None = None
    accessPoints: dict[StrictStr, AccessAnalyzerS3AccessPointConfiguration] | None = None
