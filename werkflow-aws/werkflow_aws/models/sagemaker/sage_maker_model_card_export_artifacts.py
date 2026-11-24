from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerModelCardExportArtifacts(BaseModel):
    S3ExportArtifacts: StrictStr | None = None
