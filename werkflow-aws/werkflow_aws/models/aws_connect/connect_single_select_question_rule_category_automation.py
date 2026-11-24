from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectSingleSelectQuestionRuleCategoryAutomation(BaseModel):
    Category: StrictStr | None = None
    Condition: StrictStr | None = None
    OptionRefId: StrictStr | None = None
