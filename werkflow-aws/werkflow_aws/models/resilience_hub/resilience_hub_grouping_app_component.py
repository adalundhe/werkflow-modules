from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubGroupingAppComponent(BaseModel):
    appComponentId: StrictStr | None = None
    appComponentName: StrictStr | None = None
    appComponentType: StrictStr | None = None
