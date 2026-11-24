from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class TextractCreateAdapterRequest(BaseModel):
    AdapterName: StrictStr
    FeatureTypes: list[Literal['TABLES', 'FORMS', 'QUERIES', 'SIGNATURES', 'LAYOUT']]
    ClientRequestToken: StrictStr | None = None
    Description: StrictStr | None = None
    AutoUpdate: Literal['ENABLED', 'DISABLED'] | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
