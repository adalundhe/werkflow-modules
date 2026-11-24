from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .transfer_listed_web_app import TransferListedWebApp


class TransferListWebAppsResponse(BaseModel):
    NextToken: StrictStr | None = None
    WebApps: list[TransferListedWebApp] | None = None
    ResponseMetadata: dict[str, Any] | None = None
