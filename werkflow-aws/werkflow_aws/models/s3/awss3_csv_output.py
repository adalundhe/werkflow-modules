from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AWSS3CSVOutput(BaseModel):
    QuoteFields: Literal['ALWAYS', 'ASNEEDED'] | None = None
    QuoteEscapeCharacter: StrictStr | None = None
    RecordDelimiter: StrictStr | None = None
    FieldDelimiter: StrictStr | None = None
    QuoteCharacter: StrictStr | None = None
