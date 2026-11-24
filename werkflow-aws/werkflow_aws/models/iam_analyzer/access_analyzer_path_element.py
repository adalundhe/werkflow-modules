from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .access_analyzer_substring import AccessAnalyzerSubstring


class AccessAnalyzerPathElement(BaseModel):
    index: StrictInt | None = None
    key: StrictStr | None = None
    substring: AccessAnalyzerSubstring | None = None
    value: StrictStr | None = None
