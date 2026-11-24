from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_image_static_file import QuickSightImageStaticFile
from .quick_sight_spatial_static_file import QuickSightSpatialStaticFile


class QuickSightStaticFile(BaseModel):
    ImageStaticFile: QuickSightImageStaticFile | None = None
    SpatialStaticFile: QuickSightSpatialStaticFile | None = None
