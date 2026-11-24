from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierCSVOutput(BaseModel):
    QuoteFields: StrictStr | None = None
    QuoteEscapeCharacter: StrictStr | None = None
    RecordDelimiter: StrictStr | None = None
    FieldDelimiter: StrictStr | None = None
    QuoteCharacter: StrictStr | None = None
