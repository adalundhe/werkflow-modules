from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class FieldSchemeToProjectsPartialFailure(BaseModel):
    error: StrictStr | None = None
    projectId: StrictInt | None = None
    schemeId: StrictInt | None = None
    success: StrictBool | None = None
