from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class GlueViewRepresentationInput(BaseModel):
    Dialect: Literal['REDSHIFT', 'ATHENA', 'SPARK'] | None = None
    DialectVersion: StrictStr | None = None
    ViewOriginalText: StrictStr | None = None
    ValidationConnection: StrictStr | None = None
    ViewExpandedText: StrictStr | None = None
