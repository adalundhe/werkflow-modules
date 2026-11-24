from __future__ import annotations
from pydantic import BaseModel
from .io_t_propagating_attribute import IoTPropagatingAttribute


class IoTMqtt5Configuration(BaseModel):
    propagatingAttributes: list[IoTPropagatingAttribute] | None = None
