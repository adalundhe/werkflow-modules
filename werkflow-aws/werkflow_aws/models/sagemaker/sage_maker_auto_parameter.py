from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAutoParameter(BaseModel):
    Name: StrictStr | None = None
    ValueHint: StrictStr | None = None
