from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_s3_files_location import DataZoneS3FilesLocation


class DataZoneSourceLocation(BaseModel):
    s3: StrictStr | None = None
    s3Files: DataZoneS3FilesLocation | None = None
