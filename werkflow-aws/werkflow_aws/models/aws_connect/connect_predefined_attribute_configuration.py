from __future__ import annotations
from pydantic import BaseModel, StrictBool


class ConnectPredefinedAttributeConfiguration(BaseModel):
    EnableValueValidationOnAssociation: StrictBool | None = None
    IsReadOnly: StrictBool | None = None
