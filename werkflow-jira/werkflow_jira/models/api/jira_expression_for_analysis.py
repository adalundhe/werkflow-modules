from __future__ import annotations
from pydantic import BaseModel, StrictStr


class JiraExpressionForAnalysis(BaseModel):
    contextVariables: dict[StrictStr, StrictStr] | None = None
    expressions: list[StrictStr] | None = None
