from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class SNSMessageAttributeValue(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    DataType: StrictStr
    StringValue: StrictStr | None = None
    BinaryValue: StrictBytes | BinaryIO | StrictStr | None = None
