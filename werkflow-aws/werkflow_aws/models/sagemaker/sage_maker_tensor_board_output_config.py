from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerTensorBoardOutputConfig(BaseModel):
    LocalPath: StrictStr | None = None
    S3OutputPath: StrictStr | None = None
