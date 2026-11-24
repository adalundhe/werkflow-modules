from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerSharingSettings(BaseModel):
    NotebookOutputOption: StrictStr | None = None
    S3OutputPath: StrictStr | None = None
    S3KmsKeyId: StrictStr | None = None
