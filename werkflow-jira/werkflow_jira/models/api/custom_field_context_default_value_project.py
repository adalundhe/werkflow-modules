from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CustomFieldContextDefaultValueProject(BaseModel):
    contextId: StrictStr | None = None
    projectId: StrictStr | None = None
    type: StrictStr | None = None
