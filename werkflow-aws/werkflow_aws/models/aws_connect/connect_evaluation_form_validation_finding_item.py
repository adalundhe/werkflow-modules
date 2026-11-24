from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectEvaluationFormValidationFindingItem(BaseModel):
    RefId: StrictStr | None = None
    Property: StrictStr | None = None
