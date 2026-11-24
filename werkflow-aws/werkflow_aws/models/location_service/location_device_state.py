from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .location_cell_signals import LocationCellSignals
from .location_positional_accuracy import LocationPositionalAccuracy
from .location_wi_fi_access_point import LocationWiFiAccessPoint


class LocationDeviceState(BaseModel):
    DeviceId: StrictStr
    SampleTime: datetime.datetime | StrictStr
    Position: list[StrictFloat | StrictInt]
    Accuracy: LocationPositionalAccuracy | None = None
    Ipv4Address: StrictStr | None = None
    WiFiAccessPoints: list[LocationWiFiAccessPoint] | None = None
    CellSignals: LocationCellSignals | None = None
