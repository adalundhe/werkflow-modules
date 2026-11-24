from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictBytes, StrictStr


class DynamoDBAttributeValue(BaseModel):
    S: StrictStr | None = None
    N: StrictStr | None = None
    B: StrictBytes | None = None
    SS: list[StrictStr] | None = None
    NS: list[StrictStr] | None = None
    BS: list[StrictBytes] | None = None
    M: dict[StrictStr, DynamoDBAttributeValue] | None = None
    L: list[DynamoDBAttributeValue] | None = None
    NULL: StrictBool | None = None
    BOOL: StrictBool | None = None
