from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_decal_settings import QuickSightDecalSettings


class QuickSightDecalSettingsConfiguration(BaseModel):
    CustomDecalSettings: list[QuickSightDecalSettings] | None = None
