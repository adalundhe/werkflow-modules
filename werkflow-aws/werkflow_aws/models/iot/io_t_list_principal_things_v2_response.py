from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_principal_thing_object import IoTPrincipalThingObject


class IoTListPrincipalThingsV2Response(BaseModel):
    principalThingObjects: list[IoTPrincipalThingObject] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
