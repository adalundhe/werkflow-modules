from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointEndpointDemographic(BaseModel):
    AppVersion: StrictStr | None = None
    Locale: StrictStr | None = None
    Make: StrictStr | None = None
    Model: StrictStr | None = None
    ModelVersion: StrictStr | None = None
    Platform: StrictStr | None = None
    PlatformVersion: StrictStr | None = None
    Timezone: StrictStr | None = None
