from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSStartMetadataModelAssessmentRequest(BaseModel):
    MigrationProjectIdentifier: StrictStr
    SelectionRules: StrictStr
