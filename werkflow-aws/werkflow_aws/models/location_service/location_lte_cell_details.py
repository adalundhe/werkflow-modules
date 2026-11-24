from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt
from .location_lte_local_id import LocationLteLocalId
from .location_lte_network_measurements import LocationLteNetworkMeasurements


class LocationLteCellDetails(BaseModel):
    CellId: StrictInt
    Mcc: StrictInt
    Mnc: StrictInt
    LocalId: LocationLteLocalId | None = None
    NetworkMeasurements: list[LocationLteNetworkMeasurements] | None = None
    TimingAdvance: StrictInt | None = None
    NrCapable: StrictBool | None = None
    Rsrp: StrictInt | None = None
    Rsrq: StrictFloat | StrictInt | None = None
    Tac: StrictInt | None = None
