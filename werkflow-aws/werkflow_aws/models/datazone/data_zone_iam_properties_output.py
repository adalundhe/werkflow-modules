from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DataZoneIamPropertiesOutput(BaseModel):
    environmentId: StrictStr | None = None
    glueLineageSyncEnabled: StrictBool | None = None
