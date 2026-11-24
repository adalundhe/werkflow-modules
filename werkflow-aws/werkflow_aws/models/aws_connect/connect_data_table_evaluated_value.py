from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .connect_primary_value import ConnectPrimaryValue


class ConnectDataTableEvaluatedValue(BaseModel):
    RecordId: StrictStr | None = None
    PrimaryValues: list[ConnectPrimaryValue] | None = None
    AttributeName: StrictStr | None = None
    ValueType: StrictStr | None = None
    Found: StrictBool | None = None
    Error: StrictBool | None = None
    EvaluatedValue: StrictStr | None = None
