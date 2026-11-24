from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_filter_v2_string_condition import ConnectFilterV2StringCondition


class ConnectFilterV2(BaseModel):
    FilterKey: StrictStr | None = None
    FilterValues: list[StrictStr] | None = None
    StringCondition: ConnectFilterV2StringCondition | None = None
