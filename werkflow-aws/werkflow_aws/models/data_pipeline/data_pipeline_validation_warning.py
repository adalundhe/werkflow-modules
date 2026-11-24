from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataPipelineValidationWarning(BaseModel):
    id: StrictStr | None = None
    warnings: list[StrictStr] | None = None
