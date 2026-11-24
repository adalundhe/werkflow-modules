from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftAquaConfiguration(BaseModel):
    AquaStatus: StrictStr | None = None
    AquaConfigurationStatus: StrictStr | None = None
