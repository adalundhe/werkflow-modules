from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DMSDatabaseInstanceSoftwareDetailsResponse(BaseModel):
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    EngineEdition: StrictStr | None = None
    ServicePack: StrictStr | None = None
    SupportLevel: StrictStr | None = None
    OsArchitecture: StrictInt | None = None
    Tooltip: StrictStr | None = None
