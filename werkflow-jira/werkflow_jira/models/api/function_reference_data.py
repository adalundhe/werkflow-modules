from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FunctionReferenceData(BaseModel):
    displayName: StrictStr | None = None
    isList: StrictStr | None = None
    supportsListAndSingleValueOperators: StrictStr | None = None
    types: list[StrictStr] | None = None
    value: StrictStr | None = None
