from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectMultiSelectQuestionRuleCategoryAutomation(BaseModel):
    Category: StrictStr | None = None
    Condition: StrictStr | None = None
    OptionRefIds: list[StrictStr] | None = None
