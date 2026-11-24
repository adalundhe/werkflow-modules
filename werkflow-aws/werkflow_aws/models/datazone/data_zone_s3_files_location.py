from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_s3_file import DataZoneS3File


class DataZoneS3FilesLocation(BaseModel):
    bucket: StrictStr | None = None
    fileList: list[DataZoneS3File] | None = None
