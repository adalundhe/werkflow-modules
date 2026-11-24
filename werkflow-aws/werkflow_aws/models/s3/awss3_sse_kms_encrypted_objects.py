from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3SseKmsEncryptedObjects(BaseModel):
    Status: StrictStr | None = None
