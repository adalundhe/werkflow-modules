from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_field import IoTField


class IoTThingGroupIndexingConfiguration(BaseModel):
    thingGroupIndexingMode: StrictStr | None = None
    managedFields: list[IoTField] | None = None
    customFields: list[IoTField] | None = None
