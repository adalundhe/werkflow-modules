from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CustomFieldContextUpdateDetails(BaseModel):
    description: StrictStr | None = None
    name: StrictStr | None = None
