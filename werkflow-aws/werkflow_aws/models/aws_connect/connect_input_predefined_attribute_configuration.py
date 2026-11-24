from __future__ import annotations
from pydantic import BaseModel, StrictBool


class ConnectInputPredefinedAttributeConfiguration(BaseModel):
    EnableValueValidationOnAssociation: StrictBool | None = None
