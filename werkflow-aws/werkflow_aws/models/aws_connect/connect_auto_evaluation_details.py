from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ConnectAutoEvaluationDetails(BaseModel):
    AutoEvaluationEnabled: StrictBool | None = None
    AutoEvaluationStatus: StrictStr | None = None
