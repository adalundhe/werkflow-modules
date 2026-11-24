from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieSensitivityInspectionTemplateExcludes(BaseModel):
    managedDataIdentifierIds: list[StrictStr] | None = None
