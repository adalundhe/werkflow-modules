from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranscribeTranscript(BaseModel):
    TranscriptFileUri: StrictStr | None = None
    RedactedTranscriptFileUri: StrictStr | None = None
