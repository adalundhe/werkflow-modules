from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_input_column import QuickSightInputColumn
from .quick_sight_upload_settings import QuickSightUploadSettings


class QuickSightFileSource(BaseModel):
    DataSourceArn: StrictStr | None = None
    UploadSettings: QuickSightUploadSettings | None = None
    SheetIndex: StrictInt | None = None
    InputColumns: list[QuickSightInputColumn] | None = None
