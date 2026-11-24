from __future__ import annotations
from pydantic import BaseModel, StrictBool


class EC2GetAllowedImagesSettingsRequest(BaseModel):
    DryRun: StrictBool | None = None
