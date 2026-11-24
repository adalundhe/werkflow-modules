from __future__ import annotations
from pydantic import BaseModel, StrictStr


class JiraExpressionComplexity(BaseModel):
    expensiveOperations: StrictStr | None = None
    variables: dict[StrictStr, StrictStr] | None = None
