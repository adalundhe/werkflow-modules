from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .batch_secret import BatchSecret


class BatchLogConfiguration(BaseModel):
    logDriver: StrictStr | None = None
    options: dict[StrictStr, StrictStr] | None = None
    secretOptions: list[BatchSecret] | None = None
