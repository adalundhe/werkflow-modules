from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class SESTrackingConfigurationOverrides(BaseModel):
    OpenTrackingEnabled: Literal['ENABLED', 'DISABLED'] | None = None
    ClickTrackingEnabled: Literal['ENABLED', 'DISABLED'] | None = None
