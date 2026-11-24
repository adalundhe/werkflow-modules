from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class UpdateFieldSchemeParametersPartialFailure(BaseModel):
    error: StrictStr | None = None
    fieldId: StrictStr | None = None
    schemeId: StrictInt | None = None
    success: StrictBool | None = None
    workTypeId: StrictInt | None = None
