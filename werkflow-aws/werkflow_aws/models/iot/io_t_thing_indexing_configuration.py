from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_field import IoTField
from .io_t_indexing_filter import IoTIndexingFilter


class IoTThingIndexingConfiguration(BaseModel):
    thingIndexingMode: StrictStr | None = None
    thingConnectivityIndexingMode: StrictStr | None = None
    deviceDefenderIndexingMode: StrictStr | None = None
    namedShadowIndexingMode: StrictStr | None = None
    managedFields: list[IoTField] | None = None
    customFields: list[IoTField] | None = None
    filter: IoTIndexingFilter | None = None
