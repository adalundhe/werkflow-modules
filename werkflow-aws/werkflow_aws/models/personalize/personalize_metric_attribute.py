from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeMetricAttribute(BaseModel):
    eventType: StrictStr | None = None
    metricName: StrictStr | None = None
    expression: StrictStr | None = None
