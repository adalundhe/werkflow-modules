from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .storage_gateway_chap_info import StorageGatewayChapInfo


class StorageGatewayDescribeChapCredentialsResponse(BaseModel):
    ChapCredentials: list[StorageGatewayChapInfo] | None = None
    ResponseMetadata: dict[str, Any] | None = None
