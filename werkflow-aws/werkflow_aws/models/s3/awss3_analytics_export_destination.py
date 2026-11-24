from __future__ import annotations
from pydantic import BaseModel
from .awss3_analytics_s3_bucket_destination import AWSS3AnalyticsS3BucketDestination


class AWSS3AnalyticsExportDestination(BaseModel):
    S3BucketDestination: AWSS3AnalyticsS3BucketDestination | None = None
