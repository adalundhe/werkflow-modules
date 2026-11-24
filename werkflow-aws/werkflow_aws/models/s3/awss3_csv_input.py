from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class AWSS3CSVInput(BaseModel):
    FileHeaderInfo: Literal['USE', 'IGNORE', 'NONE'] | None = None
    Comments: StrictStr | None = None
    QuoteEscapeCharacter: StrictStr | None = None
    RecordDelimiter: StrictStr | None = None
    FieldDelimiter: StrictStr | None = None
    QuoteCharacter: StrictStr | None = None
    AllowQuotedRecordDelimiter: StrictBool | None = None
