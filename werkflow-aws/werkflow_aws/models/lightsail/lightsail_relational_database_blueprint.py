from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LightsailRelationalDatabaseBlueprint(BaseModel):
    blueprintId: StrictStr | None = None
    engine: StrictStr | None = None
    engineVersion: StrictStr | None = None
    engineDescription: StrictStr | None = None
    engineVersionDescription: StrictStr | None = None
    isEngineDefault: StrictBool | None = None
