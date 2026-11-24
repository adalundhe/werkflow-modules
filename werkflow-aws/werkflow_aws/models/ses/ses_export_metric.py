from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESExportMetric(BaseModel):
    Name: StrictStr | None = None
    Aggregation: StrictStr | None = None
