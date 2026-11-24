from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDatasetSource(BaseModel):
    DatasetArn: StrictStr | None = None
