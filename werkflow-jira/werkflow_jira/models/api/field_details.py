from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field as PydanticField, StrictBool, StrictStr
from .json_type_bean import JsonTypeBean
from .scope import Scope


class FieldDetails(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    clauseNames: list[StrictStr] | None = None
    custom: StrictBool | None = None
    id: StrictStr | None = None
    key: StrictStr | None = None
    name: StrictStr | None = None
    navigable: StrictBool | None = None
    orderable: StrictBool | None = None
    schema_: JsonTypeBean | None = PydanticField(default=None, alias='schema')
    scope: Scope | None = None
    searchable: StrictBool | None = None
