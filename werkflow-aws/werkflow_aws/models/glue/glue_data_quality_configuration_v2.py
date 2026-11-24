from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class GlueDataQualityConfigurationV2(BaseModel):
    ObservationsEnabled: Literal['ALL', 'NONE'] | None = None
    ObservationMode: Literal['SCHEDULED', 'FIXED'] | None = None
