from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .transfer_described_web_app import TransferDescribedWebApp


class TransferDescribeWebAppResponse(BaseModel):
    WebApp: TransferDescribedWebApp | None = None
    ResponseMetadata: dict[str, Any] | None = None
