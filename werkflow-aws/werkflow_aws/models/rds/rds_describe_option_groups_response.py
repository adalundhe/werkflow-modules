from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rds_option_group import RDSOptionGroup


class RDSDescribeOptionGroupsResponse(BaseModel):
    OptionGroupsList: list[RDSOptionGroup] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
