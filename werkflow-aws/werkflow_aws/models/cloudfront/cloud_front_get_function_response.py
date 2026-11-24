from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class CloudFrontGetFunctionResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    FunctionCode: StrictBytes | Any | None = None
    ETag: StrictStr | None = None
    ContentType: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
