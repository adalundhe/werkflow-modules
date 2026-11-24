from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, Field as PydanticField, StrictBool, StrictStr
from .json_type_bean import JsonTypeBean


class FieldCreateMetadata(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    allowedValues: list[Any] | None = None
    autoCompleteUrl: StrictStr | None = None
    configuration: dict[StrictStr, Any] | None = None
    defaultValue: Any = None
    fieldId: StrictStr | None = None
    hasDefaultValue: StrictBool | None = None
    key: StrictStr | None = None
    name: StrictStr | None = None
    operations: list[StrictStr] | None = None
    required: StrictBool | None = None
    schema_: JsonTypeBean | None = PydanticField(default=None, alias='schema')
