from __future__ import annotations
from pydantic import BaseModel
from .glue_cloud_watch_encryption import GlueCloudWatchEncryption
from .glue_data_quality_encryption import GlueDataQualityEncryption
from .glue_job_bookmarks_encryption import GlueJobBookmarksEncryption
from .glue_s3_encryption import GlueS3Encryption


class GlueEncryptionConfiguration(BaseModel):
    S3Encryption: list[GlueS3Encryption] | None = None
    CloudWatchEncryption: GlueCloudWatchEncryption | None = None
    JobBookmarksEncryption: GlueJobBookmarksEncryption | None = None
    DataQualityEncryption: GlueDataQualityEncryption | None = None
