from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AppStreamCreateUpdatedImageRequest(BaseModel):
    existingImageName: StrictStr
    newImageName: StrictStr
    newImageDescription: StrictStr | None = None
    newImageDisplayName: StrictStr | None = None
    newImageTags: dict[StrictStr, StrictStr] | None = None
    dryRun: StrictBool | None = None
