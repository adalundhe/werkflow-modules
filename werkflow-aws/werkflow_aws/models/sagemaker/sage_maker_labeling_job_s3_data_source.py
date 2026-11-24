from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerLabelingJobS3DataSource(BaseModel):
    ManifestS3Uri: StrictStr | None = None
