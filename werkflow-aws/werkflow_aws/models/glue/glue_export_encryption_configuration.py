from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueExportEncryptionConfiguration(BaseModel):
    SseAlgorithm: StrictStr | None = None
    KmsKeyArn: StrictStr | None = None
