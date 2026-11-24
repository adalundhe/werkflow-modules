from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectEvaluationNote(BaseModel):
    Value: StrictStr | None = None
