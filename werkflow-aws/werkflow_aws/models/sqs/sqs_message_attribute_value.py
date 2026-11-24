from __future__ import annotations
from pydantic import BaseModel, StrictBytes, StrictStr


class SQSMessageAttributeValue(BaseModel):
    StringValue: StrictStr | None = None
    BinaryValue: StrictBytes | None = None
    StringListValues: list[StrictStr] | None = None
    BinaryListValues: list[StrictBytes] | None = None
    DataType: StrictStr | None = None
