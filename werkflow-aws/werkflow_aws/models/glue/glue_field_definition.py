from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .glue_filter_overrides import GlueFilterOverrides


class GlueFieldDefinition(BaseModel):
    Name: StrictStr | None = None
    FieldDataType: StrictStr | None = None
    ResponseDateFormat: StrictStr | None = None
    IsPartitionable: StrictBool | None = None
    IsNullable: StrictBool | None = None
    IsQueryable: StrictBool | None = None
    IsOrderable: StrictBool | None = None
    FilterOverrides: GlueFilterOverrides | None = None
