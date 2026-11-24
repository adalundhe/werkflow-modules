from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_microsoft_purview_provider_config import QuickSightMicrosoftPurviewProviderConfig


class QuickSightProviderConfig(BaseModel):
    MicrosoftPurview: QuickSightMicrosoftPurviewProviderConfig | None = None
