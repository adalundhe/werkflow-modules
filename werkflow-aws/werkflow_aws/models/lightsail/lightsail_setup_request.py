from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailSetupRequest(BaseModel):
    instanceName: StrictStr | None = None
    domainNames: list[StrictStr] | None = None
    certificateProvider: StrictStr | None = None
