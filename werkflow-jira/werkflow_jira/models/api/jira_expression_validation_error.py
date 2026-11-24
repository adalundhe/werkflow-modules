from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class JiraExpressionValidationError(BaseModel):
    column: StrictInt | None = None
    expression: StrictStr | None = None
    line: StrictInt | None = None
    message: StrictStr | None = None
    type: StrictStr | None = None
