from __future__ import annotations
from pydantic import BaseModel, StrictStr


class HealthImagingSort(BaseModel):
    sortOrder: StrictStr | None = None
    sortField: StrictStr | None = None
