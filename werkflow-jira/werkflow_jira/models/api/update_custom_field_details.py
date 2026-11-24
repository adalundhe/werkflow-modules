from __future__ import annotations
from pydantic import BaseModel, StrictStr


class UpdateCustomFieldDetails(BaseModel):
    description: StrictStr | None = None
    name: StrictStr | None = None
    searcherKey: StrictStr | None = None
