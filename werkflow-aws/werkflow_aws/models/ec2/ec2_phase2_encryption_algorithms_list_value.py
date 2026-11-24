from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2Phase2EncryptionAlgorithmsListValue(BaseModel):
    Value: StrictStr | None = None
