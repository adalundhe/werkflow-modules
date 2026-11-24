from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectDeactivateEvaluationFormResponse(BaseModel):
    EvaluationFormId: StrictStr | None = None
    EvaluationFormArn: StrictStr | None = None
    EvaluationFormVersion: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
