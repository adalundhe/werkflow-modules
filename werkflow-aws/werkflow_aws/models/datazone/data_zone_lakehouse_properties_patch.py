from __future__ import annotations
from pydantic import BaseModel, StrictBool


class DataZoneLakehousePropertiesPatch(BaseModel):
    glueLineageSyncEnabled: StrictBool | None = None
