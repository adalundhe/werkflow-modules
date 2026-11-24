from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .location_place_geometry import LocationPlaceGeometry
from .location_time_zone import LocationTimeZone


class LocationPlace(BaseModel):
    Label: StrictStr | None = None
    Geometry: LocationPlaceGeometry | None = None
    AddressNumber: StrictStr | None = None
    Street: StrictStr | None = None
    Neighborhood: StrictStr | None = None
    Municipality: StrictStr | None = None
    SubRegion: StrictStr | None = None
    Region: StrictStr | None = None
    Country: StrictStr | None = None
    PostalCode: StrictStr | None = None
    Interpolated: StrictBool | None = None
    TimeZone: LocationTimeZone | None = None
    UnitType: StrictStr | None = None
    UnitNumber: StrictStr | None = None
    Categories: list[StrictStr] | None = None
    SupplementalCategories: list[StrictStr] | None = None
    SubMunicipality: StrictStr | None = None
