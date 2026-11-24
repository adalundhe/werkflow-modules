from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class FieldSchemeToFieldsPartialFailure(BaseModel):
    error: StrictStr | None = None
    fieldId: StrictStr | None = None
    schemeId: StrictInt | None = None
    success: StrictBool | None = None
    workTypeIds: list[StrictInt] | None = None
