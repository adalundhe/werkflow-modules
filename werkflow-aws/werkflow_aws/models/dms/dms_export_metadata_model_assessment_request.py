from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DMSExportMetadataModelAssessmentRequest(BaseModel):
    MigrationProjectIdentifier: StrictStr
    SelectionRules: StrictStr
    FileName: StrictStr | None = None
    AssessmentReportTypes: list[Literal['pdf', 'csv']] | None = None
