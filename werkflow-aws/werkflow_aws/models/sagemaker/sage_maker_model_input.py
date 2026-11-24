from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerModelInput(BaseModel):
    DataInputConfig: StrictStr | None = None
