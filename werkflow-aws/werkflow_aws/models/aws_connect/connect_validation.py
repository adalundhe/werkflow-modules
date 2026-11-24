from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt
from .connect_validation_enum import ConnectValidationEnum


class ConnectValidation(BaseModel):
    MinLength: StrictInt | None = None
    MaxLength: StrictInt | None = None
    MinValues: StrictInt | None = None
    MaxValues: StrictInt | None = None
    IgnoreCase: StrictBool | None = None
    Minimum: StrictFloat | StrictInt | None = None
    Maximum: StrictFloat | StrictInt | None = None
    ExclusiveMinimum: StrictFloat | StrictInt | None = None
    ExclusiveMaximum: StrictFloat | StrictInt | None = None
    MultipleOf: StrictFloat | StrictInt | None = None
    Enum: ConnectValidationEnum | None = None
