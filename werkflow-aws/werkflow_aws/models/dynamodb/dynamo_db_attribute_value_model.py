from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBool, StrictBytes, StrictStr


class DynamoDBAttributeValueModel(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    S: StrictStr | None = None
    N: StrictStr | None = None
    B: StrictBytes | Any | None = None
    SS: list[StrictStr] | None = None
    NS: list[StrictStr] | None = None
    BS: list[StrictBytes | Any] | None = None
    M: dict[StrictStr, DynamoDBAttributeValueModel] | None = None
    L: list[DynamoDBAttributeValueModel] | None = None
    NULL: StrictBool | None = None
    BOOL: StrictBool | None = None
