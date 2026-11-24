from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSExportMetadataModelAssessmentResultEntry(BaseModel):
    S3ObjectKey: StrictStr | None = None
    ObjectURL: StrictStr | None = None
