from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class BedrockByteContentDoc(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    identifier: StrictStr | None = None
    contentType: StrictStr | None = None
    data: StrictBytes | Any | None = None
