from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerTensorBoardOutputConfigModel(BaseModel):
    LocalPath: StrictStr | None = None
    S3OutputPath: StrictStr | None = None
