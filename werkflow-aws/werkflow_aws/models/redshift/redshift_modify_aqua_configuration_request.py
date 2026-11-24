from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class RedshiftModifyAquaConfigurationRequest(BaseModel):
    ClusterIdentifier: StrictStr
    AquaConfigurationStatus: Literal['enabled', 'disabled', 'auto'] | None = None
