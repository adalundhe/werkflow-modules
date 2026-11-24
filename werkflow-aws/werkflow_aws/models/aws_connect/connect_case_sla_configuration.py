from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_field_value_union import ConnectFieldValueUnion


class ConnectCaseSlaConfiguration(BaseModel):
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    FieldId: StrictStr | None = None
    TargetFieldValues: list[ConnectFieldValueUnion] | None = None
    TargetSlaMinutes: StrictInt | None = None
