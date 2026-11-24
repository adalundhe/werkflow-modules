from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerPropertyNameSuggestion(BaseModel):
    PropertyName: StrictStr | None = None
