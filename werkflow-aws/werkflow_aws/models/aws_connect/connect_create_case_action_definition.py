from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_field_value import ConnectFieldValue


class ConnectCreateCaseActionDefinition(BaseModel):
    Fields: list[ConnectFieldValue] | None = None
    TemplateId: StrictStr | None = None
