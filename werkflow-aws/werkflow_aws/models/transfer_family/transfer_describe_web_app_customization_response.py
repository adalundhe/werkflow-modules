from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .transfer_described_web_app_customization import TransferDescribedWebAppCustomization


class TransferDescribeWebAppCustomizationResponse(BaseModel):
    WebAppCustomization: TransferDescribedWebAppCustomization | None = None
    ResponseMetadata: dict[str, Any] | None = None
