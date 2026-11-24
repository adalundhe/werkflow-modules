from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeHPOObjective(BaseModel):
    type: StrictStr | None = None
    metricName: StrictStr | None = None
    metricRegex: StrictStr | None = None
