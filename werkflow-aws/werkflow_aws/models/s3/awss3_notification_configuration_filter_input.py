from __future__ import annotations
from pydantic import BaseModel
from .awss3_s3_key_filter_input import AWSS3S3KeyFilterInput


class AWSS3NotificationConfigurationFilterInput(BaseModel):
    Key: AWSS3S3KeyFilterInput | None = None
