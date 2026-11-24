from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_table_field_image_configuration import QuickSightTableFieldImageConfiguration
from .quick_sight_table_field_link_configuration import QuickSightTableFieldLinkConfiguration


class QuickSightTableFieldURLConfiguration(BaseModel):
    LinkConfiguration: QuickSightTableFieldLinkConfiguration | None = None
    ImageConfiguration: QuickSightTableFieldImageConfiguration | None = None
