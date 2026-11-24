from __future__ import annotations
from pydantic import BaseModel, StrictBool


class DataZoneIamPropertiesPatch(BaseModel):
    glueLineageSyncEnabled: StrictBool | None = None
