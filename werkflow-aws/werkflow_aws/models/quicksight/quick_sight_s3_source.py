from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_input_column import QuickSightInputColumn
from .quick_sight_upload_settings import QuickSightUploadSettings


class QuickSightS3Source(BaseModel):
    DataSourceArn: StrictStr | None = None
    UploadSettings: QuickSightUploadSettings | None = None
    InputColumns: list[QuickSightInputColumn] | None = None
