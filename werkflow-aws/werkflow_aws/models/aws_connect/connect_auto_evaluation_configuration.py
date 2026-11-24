from __future__ import annotations
from pydantic import BaseModel, StrictBool


class ConnectAutoEvaluationConfiguration(BaseModel):
    Enabled: StrictBool
