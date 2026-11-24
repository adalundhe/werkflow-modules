from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerModelSpeculativeDecodingTrainingDataSource(BaseModel):
    S3Uri: StrictStr | None = None
    S3DataType: StrictStr | None = None
