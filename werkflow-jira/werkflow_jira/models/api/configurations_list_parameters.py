from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigurationsListParameters(BaseModel):
    fieldIdsOrKeys: list[StrictStr] | None = None
