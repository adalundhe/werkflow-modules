from __future__ import annotations
from pydantic import BaseModel
from .awss3_s3_key_filter import AWSS3S3KeyFilter


class AWSS3NotificationConfigurationFilter(BaseModel):
    Key: AWSS3S3KeyFilter | None = None
