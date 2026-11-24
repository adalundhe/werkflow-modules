from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueFilterStringConfiguration(BaseModel):
    QueryParameterName: StrictStr | None = None
    QuoteStringValues: StrictBool | None = None
    QuoteCharacter: StrictStr | None = None
