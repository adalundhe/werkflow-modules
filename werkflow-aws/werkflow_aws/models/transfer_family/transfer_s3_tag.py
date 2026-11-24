from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferS3Tag(BaseModel):
    Key: StrictStr | None = None
    Value: StrictStr | None = None
