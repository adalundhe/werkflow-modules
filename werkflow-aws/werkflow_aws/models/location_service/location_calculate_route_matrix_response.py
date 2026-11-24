from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictFloat, StrictInt
from .location_calculate_route_matrix_summary import LocationCalculateRouteMatrixSummary
from .location_route_matrix_entry import LocationRouteMatrixEntry


class LocationCalculateRouteMatrixResponse(BaseModel):
    RouteMatrix: list[list[LocationRouteMatrixEntry]] | None = None
    SnappedDeparturePositions: list[list[StrictFloat | StrictInt]] | None = None
    SnappedDestinationPositions: list[list[StrictFloat | StrictInt]] | None = None
    Summary: LocationCalculateRouteMatrixSummary | None = None
    ResponseMetadata: dict[str, Any] | None = None
