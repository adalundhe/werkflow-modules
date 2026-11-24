from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecr_public_registry import ECRPublicRegistry


class ECRPublicDescribeRegistriesResponse(BaseModel):
    registries: list[ECRPublicRegistry] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
