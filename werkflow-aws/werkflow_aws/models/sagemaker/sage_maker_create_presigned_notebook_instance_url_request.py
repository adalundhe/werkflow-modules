from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerCreatePresignedNotebookInstanceUrlRequest(BaseModel):
    NotebookInstanceName: StrictStr
    SessionExpirationDurationInSeconds: StrictInt | None = None
