from __future__ import annotations
from pydantic import BaseModel, StrictBool


class ConnectEvaluationFormAutoEvaluationConfiguration(BaseModel):
    Enabled: StrictBool | None = None
