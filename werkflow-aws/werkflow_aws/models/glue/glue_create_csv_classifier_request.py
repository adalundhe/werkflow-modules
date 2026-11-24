from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class GlueCreateCsvClassifierRequest(BaseModel):
    Name: StrictStr
    Delimiter: StrictStr | None = None
    QuoteSymbol: StrictStr | None = None
    ContainsHeader: Literal['UNKNOWN', 'PRESENT', 'ABSENT'] | None = None
    Header: list[StrictStr] | None = None
    DisableValueTrimming: StrictBool | None = None
    AllowSingleColumn: StrictBool | None = None
    CustomDatatypeConfigured: StrictBool | None = None
    CustomDatatypes: list[StrictStr] | None = None
    Serde: Literal['OpenCSVSerDe', 'LazySimpleSerDe', 'None'] | None = None
