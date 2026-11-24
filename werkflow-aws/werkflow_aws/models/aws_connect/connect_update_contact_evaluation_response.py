from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ConnectUpdateContactEvaluationResponse(BaseModel):
    EvaluationId: StrictStr | None = None
    EvaluationArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
