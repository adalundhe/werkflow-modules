from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, Field as PydanticField, StrictStr


class ContextualConfiguration(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    configuration: Any = None
    fieldContextId: StrictStr | None = None
    id: StrictStr | None = None
    schema_: Any = PydanticField(default=None, alias='schema')
