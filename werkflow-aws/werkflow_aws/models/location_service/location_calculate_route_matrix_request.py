from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .location_calculate_route_car_mode_options import LocationCalculateRouteCarModeOptions
from .location_calculate_route_truck_mode_options import LocationCalculateRouteTruckModeOptions


class LocationCalculateRouteMatrixRequest(BaseModel):
    CalculatorName: StrictStr
    DeparturePositions: list[list[StrictFloat | StrictInt]]
    DestinationPositions: list[list[StrictFloat | StrictInt]]
    TravelMode: Literal['Car', 'Truck', 'Walking', 'Bicycle', 'Motorcycle'] | None = None
    DepartureTime: datetime.datetime | StrictStr | None = None
    DepartNow: StrictBool | None = None
    DistanceUnit: Literal['Kilometers', 'Miles'] | None = None
    CarModeOptions: LocationCalculateRouteCarModeOptions | None = None
    TruckModeOptions: LocationCalculateRouteTruckModeOptions | None = None
    Key: StrictStr | None = None
