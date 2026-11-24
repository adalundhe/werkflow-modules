from __future__ import annotations
from pydantic import BaseModel, StrictBool


class DataZoneLakehousePropertiesInput(BaseModel):
    glueLineageSyncEnabled: StrictBool | None = None
