from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class MWAACreateWebLoginTokenResponse(BaseModel):
    WebToken: StrictStr | None = None
    WebServerHostname: StrictStr | None = None
    IamIdentity: StrictStr | None = None
    AirflowIdentity: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
