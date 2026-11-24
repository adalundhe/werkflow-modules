from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockEvaluatorModel(BaseModel):
    modelIdentifier: StrictStr | None = None
