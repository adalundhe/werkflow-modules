from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ECSTaskEphemeralStorage(BaseModel):
    sizeInGiB: StrictInt | None = None
    kmsKeyId: StrictStr | None = None
