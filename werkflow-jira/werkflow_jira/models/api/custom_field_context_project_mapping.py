from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CustomFieldContextProjectMapping(BaseModel):
    contextId: StrictStr | None = None
    isGlobalContext: StrictBool | None = None
    projectId: StrictStr | None = None
