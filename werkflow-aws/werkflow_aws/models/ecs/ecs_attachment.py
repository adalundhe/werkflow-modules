from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_key_value_pair import ECSKeyValuePair


class ECSAttachment(BaseModel):
    id: StrictStr | None = None
    type: StrictStr | None = None
    status: StrictStr | None = None
    details: list[ECSKeyValuePair] | None = None
