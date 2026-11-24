from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionMediaAnalysisOutputConfig(BaseModel):
    S3Bucket: StrictStr | None = None
    S3KeyPrefix: StrictStr | None = None
