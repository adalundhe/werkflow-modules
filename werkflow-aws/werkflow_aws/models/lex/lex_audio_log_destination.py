from __future__ import annotations
from pydantic import BaseModel
from .lex_s3_bucket_log_destination import LexS3BucketLogDestination


class LexAudioLogDestination(BaseModel):
    s3Bucket: LexS3BucketLogDestination | None = None
