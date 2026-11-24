from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerModelCardExportOutputConfig(BaseModel):
    S3OutputPath: StrictStr | None = None
