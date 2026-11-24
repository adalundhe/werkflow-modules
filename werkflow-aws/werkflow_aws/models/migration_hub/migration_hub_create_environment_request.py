from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class MigrationHubCreateEnvironmentRequest(BaseModel):
    Name: StrictStr
    NetworkFabricType: Literal['TRANSIT_GATEWAY', 'NONE']
    ClientToken: StrictStr | None = None
    Description: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
