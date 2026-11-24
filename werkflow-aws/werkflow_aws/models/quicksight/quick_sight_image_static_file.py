from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_static_file_source import QuickSightStaticFileSource


class QuickSightImageStaticFile(BaseModel):
    StaticFileId: StrictStr | None = None
    Source: QuickSightStaticFileSource | None = None
