from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AppFlowDestinationFieldProperties(BaseModel):
    isCreatable: StrictBool | None = None
    isNullable: StrictBool | None = None
    isUpsertable: StrictBool | None = None
    isUpdatable: StrictBool | None = None
    isDefaultedOnCreate: StrictBool | None = None
    supportedWriteOperations: list[StrictStr] | None = None
