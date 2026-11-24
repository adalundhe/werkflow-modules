from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class QuickSightUploadSettings(BaseModel):
    Format: StrictStr | None = None
    StartFromRow: StrictInt | None = None
    ContainsHeader: StrictBool | None = None
    TextQualifier: StrictStr | None = None
    Delimiter: StrictStr | None = None
    CustomCellAddressRange: StrictStr | None = None
