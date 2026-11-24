from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerSpaceSharingSettingsSummary(BaseModel):
    SharingType: StrictStr | None = None
