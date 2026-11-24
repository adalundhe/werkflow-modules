from __future__ import annotations
from pydantic import BaseModel, StrictStr


class UpdateFieldConfigurationSchemeDetails(BaseModel):
    description: StrictStr | None = None
    name: StrictStr | None = None
