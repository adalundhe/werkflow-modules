from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_geospatial_static_file_source import QuickSightGeospatialStaticFileSource


class QuickSightGeospatialDataSourceItem(BaseModel):
    StaticFileDataSource: QuickSightGeospatialStaticFileSource | None = None
