from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightWordCloudOptions(BaseModel):
    WordOrientation: StrictStr | None = None
    WordScaling: StrictStr | None = None
    CloudLayout: StrictStr | None = None
    WordCasing: StrictStr | None = None
    WordPadding: StrictStr | None = None
    MaximumStringLength: StrictInt | None = None
