from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerSpaceSharingSettings(BaseModel):
    SharingType: StrictStr | None = None
