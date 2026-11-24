from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class FieldConfigurationItem(BaseModel):
    description: StrictStr | None = None
    id: StrictStr | None = None
    isHidden: StrictBool | None = None
    isRequired: StrictBool | None = None
    renderer: StrictStr | None = None
