from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ConnectCreateEvaluationFormResponse(BaseModel):
    EvaluationFormId: StrictStr | None = None
    EvaluationFormArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
