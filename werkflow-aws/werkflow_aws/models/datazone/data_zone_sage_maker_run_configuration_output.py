from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneSageMakerRunConfigurationOutput(BaseModel):
    accountId: StrictStr | None = None
    region: StrictStr | None = None
    trackingAssets: dict[StrictStr, list[StrictStr]] | None = None
