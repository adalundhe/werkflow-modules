from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glacier_provisioned_capacity_description import GlacierProvisionedCapacityDescription


class GlacierListProvisionedCapacityResponse(BaseModel):
    ProvisionedCapacityList: list[GlacierProvisionedCapacityDescription] | None = None
    ResponseMetadata: dict[str, Any] | None = None
