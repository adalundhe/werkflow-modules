from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CustomFieldContextDefaultValueLabels(BaseModel):
    contextId: StrictStr | None = None
    labels: list[StrictStr] | None = None
    type: StrictStr | None = None
