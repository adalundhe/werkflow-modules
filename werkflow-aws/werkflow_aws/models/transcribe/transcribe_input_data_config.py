from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranscribeInputDataConfig(BaseModel):
    S3Uri: StrictStr | None = None
    TuningDataS3Uri: StrictStr | None = None
    DataAccessRoleArn: StrictStr | None = None
