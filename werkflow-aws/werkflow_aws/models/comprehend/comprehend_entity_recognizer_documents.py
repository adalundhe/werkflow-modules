from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendEntityRecognizerDocuments(BaseModel):
    S3Uri: StrictStr | None = None
    TestS3Uri: StrictStr | None = None
    InputFormat: StrictStr | None = None
