from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieAwsService(BaseModel):
    invokedBy: StrictStr | None = None
