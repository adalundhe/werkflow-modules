from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_post_accept_timeout_config import ConnectPostAcceptTimeoutConfig


class ConnectPreview(BaseModel):
    PostAcceptTimeoutConfig: ConnectPostAcceptTimeoutConfig | None = None
    AllowedUserActions: list[StrictStr] | None = None
