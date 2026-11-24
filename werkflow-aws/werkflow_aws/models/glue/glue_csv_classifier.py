from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class GlueCsvClassifier(BaseModel):
    Name: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastUpdated: datetime.datetime | StrictStr | None = None
    Version: StrictInt | None = None
    Delimiter: StrictStr | None = None
    QuoteSymbol: StrictStr | None = None
    ContainsHeader: StrictStr | None = None
    Header: list[StrictStr] | None = None
    DisableValueTrimming: StrictBool | None = None
    AllowSingleColumn: StrictBool | None = None
    CustomDatatypeConfigured: StrictBool | None = None
    CustomDatatypes: list[StrictStr] | None = None
    Serde: StrictStr | None = None
