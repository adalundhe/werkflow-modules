from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CustomFieldDefinitionJsonBean(BaseModel):
    description: StrictStr | None = None
    name: StrictStr | None = None
    searcherKey: StrictStr | None = None
    type: StrictStr | None = None
