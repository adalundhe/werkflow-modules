from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataPipelineValidationError(BaseModel):
    id: StrictStr | None = None
    errors: list[StrictStr] | None = None
