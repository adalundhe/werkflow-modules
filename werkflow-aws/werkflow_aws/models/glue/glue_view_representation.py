from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueViewRepresentation(BaseModel):
    Dialect: StrictStr | None = None
    DialectVersion: StrictStr | None = None
    ViewOriginalText: StrictStr | None = None
    ViewExpandedText: StrictStr | None = None
    ValidationConnection: StrictStr | None = None
    IsStale: StrictBool | None = None
