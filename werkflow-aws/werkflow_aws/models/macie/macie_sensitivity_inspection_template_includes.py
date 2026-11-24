from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieSensitivityInspectionTemplateIncludes(BaseModel):
    allowListIds: list[StrictStr] | None = None
    customDataIdentifierIds: list[StrictStr] | None = None
    managedDataIdentifierIds: list[StrictStr] | None = None
