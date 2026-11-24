from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CreateCustomFieldContext(BaseModel):
    description: StrictStr | None = None
    id: StrictStr | None = None
    issueTypeIds: list[StrictStr] | None = None
    name: StrictStr | None = None
    projectIds: list[StrictStr] | None = None
