from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSGetTargetSelectionRulesRequest(BaseModel):
    MigrationProjectIdentifier: StrictStr
    SelectionRules: StrictStr
