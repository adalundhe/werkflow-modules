from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .verified_permissions_batch_is_authorized_output_item import VerifiedPermissionsBatchIsAuthorizedOutputItem


class VerifiedPermissionsBatchIsAuthorizedResponse(BaseModel):
    results: list[VerifiedPermissionsBatchIsAuthorizedOutputItem] | None = None
    ResponseMetadata: dict[str, Any] | None = None
