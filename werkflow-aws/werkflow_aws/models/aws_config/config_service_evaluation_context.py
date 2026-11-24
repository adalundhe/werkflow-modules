from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceEvaluationContext(BaseModel):
    EvaluationContextIdentifier: StrictStr | None = None
