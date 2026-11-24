from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DataZoneIamPropertiesInput(BaseModel):
    glueLineageSyncEnabled: StrictBool | None = None
    roleArn: StrictStr | None = None
