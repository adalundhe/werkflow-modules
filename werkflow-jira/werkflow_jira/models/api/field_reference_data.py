from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FieldReferenceData(BaseModel):
    auto: StrictStr | None = None
    cfid: StrictStr | None = None
    deprecated: StrictStr | None = None
    deprecatedSearcherKey: StrictStr | None = None
    displayName: StrictStr | None = None
    operators: list[StrictStr] | None = None
    orderable: StrictStr | None = None
    searchable: StrictStr | None = None
    types: list[StrictStr] | None = None
    value: StrictStr | None = None
