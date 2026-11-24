from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dms_export_metadata_model_assessment_result_entry import DMSExportMetadataModelAssessmentResultEntry


class DMSExportMetadataModelAssessmentResponse(BaseModel):
    PdfReport: DMSExportMetadataModelAssessmentResultEntry | None = None
    CsvReport: DMSExportMetadataModelAssessmentResultEntry | None = None
    ResponseMetadata: dict[str, Any] | None = None
