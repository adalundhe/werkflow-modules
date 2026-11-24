from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field as PydanticField, StrictBool, StrictInt, StrictStr
from .field_last_used import FieldLastUsed
from .json_type_bean import JsonTypeBean


class Field(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    contextsCount: StrictInt | None = None
    description: StrictStr | None = None
    id: StrictStr | None = None
    isLocked: StrictBool | None = None
    isUnscreenable: StrictBool | None = None
    key: StrictStr | None = None
    lastUsed: FieldLastUsed | None = None
    name: StrictStr | None = None
    projectsCount: StrictInt | None = None
    schema_: JsonTypeBean | None = PydanticField(default=None, alias='schema')
    screensCount: StrictInt | None = None
    searcherKey: StrictStr | None = None
    stableId: StrictStr | None = None
    translatedDescription: StrictStr | None = None
    translatedName: StrictStr | None = None
    typeDisplayName: StrictStr | None = None
