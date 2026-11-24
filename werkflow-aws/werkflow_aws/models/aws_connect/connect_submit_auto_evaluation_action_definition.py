from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectSubmitAutoEvaluationActionDefinition(BaseModel):
    EvaluationFormId: StrictStr | None = None
