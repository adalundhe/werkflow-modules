from __future__ import annotations
from pydantic import BaseModel
from .lightsail_instance_entry import LightsailInstanceEntry


class LightsailCreateCloudFormationStackRequest(BaseModel):
    instances: list[LightsailInstanceEntry]
