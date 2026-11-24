from __future__ import annotations
from pydantic import BaseModel, StrictInt


class QuickSightPluginVisualItemsLimitConfiguration(BaseModel):
    ItemsLimit: StrictInt | None = None
