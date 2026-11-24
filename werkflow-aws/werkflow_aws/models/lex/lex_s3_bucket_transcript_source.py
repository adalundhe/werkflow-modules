from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_path_format import LexPathFormat
from .lex_transcript_filter import LexTranscriptFilter


class LexS3BucketTranscriptSource(BaseModel):
    s3BucketName: StrictStr | None = None
    pathFormat: LexPathFormat | None = None
    transcriptFormat: StrictStr | None = None
    transcriptFilter: LexTranscriptFilter | None = None
    kmsKeyArn: StrictStr | None = None
