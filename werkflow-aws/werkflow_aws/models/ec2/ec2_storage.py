from __future__ import annotations
from pydantic import BaseModel
from .ec2_s3_storage import EC2S3Storage


class EC2Storage(BaseModel):
    S3: EC2S3Storage | None = None
