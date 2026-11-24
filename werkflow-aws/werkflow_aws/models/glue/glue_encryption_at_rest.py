from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueEncryptionAtRest(BaseModel):
    CatalogEncryptionMode: StrictStr | None = None
    SseAwsKmsKeyId: StrictStr | None = None
    CatalogEncryptionServiceRole: StrictStr | None = None
