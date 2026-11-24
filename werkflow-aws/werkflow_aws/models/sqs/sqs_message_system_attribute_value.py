from __future__ import annotations
from pydantic import BaseModel, StrictBytes, StrictStr


class SQSMessageSystemAttributeValue(BaseModel):
    DataType: StrictStr
    StringValue: StrictStr | None = None
    BinaryValue: StrictBytes | None = None
    StringListValues: list[StrictStr] | None = None
    BinaryListValues: list[StrictBytes] | None = None
