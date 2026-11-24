from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .location_calculate_route_car_mode_options import LocationCalculateRouteCarModeOptions
from .location_calculate_route_truck_mode_options import LocationCalculateRouteTruckModeOptions


class LocationCalculateRouteRequest(BaseModel):
    CalculatorName: StrictStr
    DeparturePosition: list[StrictFloat | StrictInt]
    DestinationPosition: list[StrictFloat | StrictInt]
    WaypointPositions: list[list[StrictFloat | StrictInt]] | None = None
    TravelMode: Literal['Car', 'Truck', 'Walking', 'Bicycle', 'Motorcycle'] | None = None
    DepartureTime: datetime.datetime | StrictStr | None = None
    DepartNow: StrictBool | None = None
    DistanceUnit: Literal['Kilometers', 'Miles'] | None = None
    IncludeLegGeometry: StrictBool | None = None
    CarModeOptions: LocationCalculateRouteCarModeOptions | None = None
    TruckModeOptions: LocationCalculateRouteTruckModeOptions | None = None
    ArrivalTime: datetime.datetime | StrictStr | None = None
    OptimizeFor: Literal['FastestRoute', 'ShortestRoute'] | None = None
    Key: StrictStr | None = None
