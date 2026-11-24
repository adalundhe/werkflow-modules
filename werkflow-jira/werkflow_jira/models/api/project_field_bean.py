from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ProjectFieldBean(BaseModel):
    description: StrictStr | None = None
    fieldId: StrictStr | None = None
    isRequired: StrictBool | None = None
    projectId: StrictInt | None = None
    workTypeId: StrictInt | None = None
