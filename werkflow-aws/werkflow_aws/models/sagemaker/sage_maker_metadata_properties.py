from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerMetadataProperties(BaseModel):
    CommitId: StrictStr | None = None
    Repository: StrictStr | None = None
    GeneratedBy: StrictStr | None = None
    ProjectId: StrictStr | None = None
