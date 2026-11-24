from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_sheet_image_static_file_source import QuickSightSheetImageStaticFileSource


class QuickSightSheetImageSource(BaseModel):
    SheetImageStaticFileSource: QuickSightSheetImageStaticFileSource | None = None
