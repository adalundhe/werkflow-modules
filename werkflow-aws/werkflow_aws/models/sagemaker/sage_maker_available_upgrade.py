from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAvailableUpgrade(BaseModel):
    Version: StrictStr | None = None
    ReleaseNotes: list[StrictStr] | None = None
