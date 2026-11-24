from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .connect_empty_field_value import ConnectEmptyFieldValue


class ConnectFieldValueUnion(BaseModel):
    BooleanValue: StrictBool | None = None
    DoubleValue: StrictFloat | StrictInt | None = None
    EmptyValue: ConnectEmptyFieldValue | None = None
    StringValue: StrictStr | None = None
