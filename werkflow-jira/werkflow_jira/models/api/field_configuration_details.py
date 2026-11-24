from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FieldConfigurationDetails(BaseModel):
    description: StrictStr | None = None
    name: StrictStr | None = None
