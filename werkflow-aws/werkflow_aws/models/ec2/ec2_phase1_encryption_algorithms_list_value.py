from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2Phase1EncryptionAlgorithmsListValue(BaseModel):
    Value: StrictStr | None = None
