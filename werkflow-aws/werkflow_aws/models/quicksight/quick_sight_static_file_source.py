from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_static_file_s3_source_options import QuickSightStaticFileS3SourceOptions
from .quick_sight_static_file_url_source_options import QuickSightStaticFileUrlSourceOptions


class QuickSightStaticFileSource(BaseModel):
    UrlOptions: QuickSightStaticFileUrlSourceOptions | None = None
    S3Options: QuickSightStaticFileS3SourceOptions | None = None
