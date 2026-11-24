from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rds_option_group_option import RDSOptionGroupOption


class RDSDescribeOptionGroupOptionsResponse(BaseModel):
    OptionGroupOptions: list[RDSOptionGroupOption] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
