from __future__ import annotations
from pydantic import BaseModel
from .glacier_s3_location import GlacierS3Location


class GlacierOutputLocation(BaseModel):
    S3: GlacierS3Location | None = None
