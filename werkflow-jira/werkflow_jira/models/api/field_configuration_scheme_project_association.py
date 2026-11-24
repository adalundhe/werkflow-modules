from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FieldConfigurationSchemeProjectAssociation(BaseModel):
    fieldConfigurationSchemeId: StrictStr | None = None
    projectId: StrictStr | None = None
