from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendDocumentClassifierOutputDataConfig(BaseModel):
    S3Uri: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    FlywheelStatsS3Prefix: StrictStr | None = None
