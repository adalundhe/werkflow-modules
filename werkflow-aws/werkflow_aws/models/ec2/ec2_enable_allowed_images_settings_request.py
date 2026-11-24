from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool


class EC2EnableAllowedImagesSettingsRequest(BaseModel):
    AllowedImagesSettingsState: Literal['enabled', 'audit-mode']
    DryRun: StrictBool | None = None
