from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewaySoftwareUpdatePreferences(BaseModel):
    AutomaticUpdatePolicy: StrictStr | None = None
