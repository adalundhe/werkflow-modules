from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class MWAACreateCliTokenResponse(BaseModel):
    CliToken: StrictStr | None = None
    WebServerHostname: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
