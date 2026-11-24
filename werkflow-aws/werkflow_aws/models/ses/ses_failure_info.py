from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESFailureInfo(BaseModel):
    FailedRecordsS3Url: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
