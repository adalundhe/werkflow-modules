from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class FieldAssociationParameters(BaseModel):
    description: StrictStr | None = None
    isRequired: StrictBool | None = None
    rendererType: StrictStr | None = None
