from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class EC2SecureBlobAttributeValue(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Value: StrictBytes | BinaryIO | StrictStr | None = None
