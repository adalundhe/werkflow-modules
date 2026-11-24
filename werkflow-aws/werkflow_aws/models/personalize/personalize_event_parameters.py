from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class PersonalizeEventParameters(BaseModel):
    eventType: StrictStr | None = None
    eventValueThreshold: StrictFloat | StrictInt | None = None
    weight: StrictFloat | StrictInt | None = None
