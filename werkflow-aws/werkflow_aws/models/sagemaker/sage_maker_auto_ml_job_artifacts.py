from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAutoMLJobArtifacts(BaseModel):
    CandidateDefinitionNotebookLocation: StrictStr | None = None
    DataExplorationNotebookLocation: StrictStr | None = None
