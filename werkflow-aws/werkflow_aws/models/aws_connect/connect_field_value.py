from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_field_value_union import ConnectFieldValueUnion


class ConnectFieldValue(BaseModel):
    Id: StrictStr | None = None
    Value: ConnectFieldValueUnion | None = None
