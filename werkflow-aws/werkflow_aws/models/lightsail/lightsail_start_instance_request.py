from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lightsail_instance_attribute_updates import LightsailInstanceAttributeUpdates


class LightsailStartInstanceRequest(BaseModel):
    instanceName: StrictStr
    attributeUpdates: LightsailInstanceAttributeUpdates | None = None
