from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerOwnershipSettingsSummary(BaseModel):
    OwnerUserProfileName: StrictStr | None = None
