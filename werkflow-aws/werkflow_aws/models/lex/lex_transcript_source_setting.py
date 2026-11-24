from __future__ import annotations
from pydantic import BaseModel
from .lex_s3_bucket_transcript_source import LexS3BucketTranscriptSource


class LexTranscriptSourceSetting(BaseModel):
    s3BucketTranscriptSource: LexS3BucketTranscriptSource | None = None
