from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_thing_principal_object import IoTThingPrincipalObject


class IoTListThingPrincipalsV2Response(BaseModel):
    thingPrincipalObjects: list[IoTThingPrincipalObject] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
