from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerOwnershipSettings(BaseModel):
    OwnerUserProfileName: StrictStr | None = None
