from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierCSVInput(BaseModel):
    FileHeaderInfo: StrictStr | None = None
    Comments: StrictStr | None = None
    QuoteEscapeCharacter: StrictStr | None = None
    RecordDelimiter: StrictStr | None = None
    FieldDelimiter: StrictStr | None = None
    QuoteCharacter: StrictStr | None = None
