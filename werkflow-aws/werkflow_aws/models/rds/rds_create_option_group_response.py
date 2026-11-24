from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rds_option_group import RDSOptionGroup


class RDSCreateOptionGroupResponse(BaseModel):
    OptionGroup: RDSOptionGroup | None = None
    ResponseMetadata: dict[str, Any] | None = None
