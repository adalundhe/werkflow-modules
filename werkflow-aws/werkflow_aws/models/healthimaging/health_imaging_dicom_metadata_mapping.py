from __future__ import annotations
from pydantic import BaseModel, StrictStr


class HealthImagingDicomMetadataMapping(BaseModel):
    studyInstanceUID: StrictStr | None = None
    seriesInstanceUID: StrictStr | None = None
    metadataFilePath: StrictStr | None = None
