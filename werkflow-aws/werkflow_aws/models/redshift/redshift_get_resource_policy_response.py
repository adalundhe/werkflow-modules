from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .redshift_resource_policy import RedshiftResourcePolicy


class RedshiftGetResourcePolicyResponse(BaseModel):
    ResourcePolicy: RedshiftResourcePolicy | None = None
    ResponseMetadata: dict[str, Any] | None = None
