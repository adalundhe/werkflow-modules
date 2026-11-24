from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneSageMakerRunConfigurationInput(BaseModel):
    trackingAssets: dict[StrictStr, list[StrictStr]]
