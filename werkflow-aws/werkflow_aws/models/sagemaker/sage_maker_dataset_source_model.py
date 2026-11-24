from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDatasetSourceModel(BaseModel):
    DatasetArn: StrictStr | None = None
