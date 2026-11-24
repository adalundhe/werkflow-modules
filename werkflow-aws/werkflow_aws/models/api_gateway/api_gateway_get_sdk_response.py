from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class APIGatewayGetSdkResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    contentType: StrictStr | None = None
    contentDisposition: StrictStr | None = None
    body: StrictBytes | Any | None = None
    ResponseMetadata: dict[str, Any] | None = None
