from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerKmsGrantConstraints(BaseModel):
    encryptionContextEquals: dict[StrictStr, StrictStr] | None = None
    encryptionContextSubset: dict[StrictStr, StrictStr] | None = None
