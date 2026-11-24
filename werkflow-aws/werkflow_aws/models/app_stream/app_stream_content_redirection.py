from __future__ import annotations
from pydantic import BaseModel
from .app_stream_url_redirection_config import AppStreamUrlRedirectionConfig


class AppStreamContentRedirection(BaseModel):
    HostToClient: AppStreamUrlRedirectionConfig | None = None
