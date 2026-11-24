from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .organizations_root_model import OrganizationsRootModel


class OrganizationsEnablePolicyTypeResponse(BaseModel):
    Root: OrganizationsRootModel | None = None
    ResponseMetadata: dict[str, Any] | None = None
