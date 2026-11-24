from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeAutoTrainingConfig(BaseModel):
    schedulingExpression: StrictStr | None = None
