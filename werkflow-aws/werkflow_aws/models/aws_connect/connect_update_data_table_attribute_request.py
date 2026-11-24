from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .connect_validation import ConnectValidation


class ConnectUpdateDataTableAttributeRequest(BaseModel):
    InstanceId: StrictStr
    DataTableId: StrictStr
    AttributeName: StrictStr
    Name: StrictStr
    ValueType: Literal['TEXT', 'NUMBER', 'BOOLEAN', 'TEXT_LIST', 'NUMBER_LIST']
    Description: StrictStr | None = None
    Primary: StrictBool | None = None
    Validation: ConnectValidation | None = None
