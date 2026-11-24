from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueField(BaseModel):
    FieldName: StrictStr | None = None
    Label: StrictStr | None = None
    Description: StrictStr | None = None
    FieldType: StrictStr | None = None
    IsPrimaryKey: StrictBool | None = None
    IsNullable: StrictBool | None = None
    IsRetrievable: StrictBool | None = None
    IsFilterable: StrictBool | None = None
    IsPartitionable: StrictBool | None = None
    IsCreateable: StrictBool | None = None
    IsUpdateable: StrictBool | None = None
    IsUpsertable: StrictBool | None = None
    IsDefaultOnCreate: StrictBool | None = None
    SupportedValues: list[StrictStr] | None = None
    SupportedFilterOperators: list[StrictStr] | None = None
    ParentField: StrictStr | None = None
    NativeDataType: StrictStr | None = None
    CustomProperties: dict[StrictStr, StrictStr] | None = None
