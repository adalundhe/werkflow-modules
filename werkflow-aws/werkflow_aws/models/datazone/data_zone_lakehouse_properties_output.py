from __future__ import annotations
from pydantic import BaseModel, StrictBool


class DataZoneLakehousePropertiesOutput(BaseModel):
    glueLineageSyncEnabled: StrictBool | None = None
