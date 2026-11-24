from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .glue_s3_direct_source_additional_options import GlueS3DirectSourceAdditionalOptions
from .glue_schema import GlueSchema


class GlueS3ParquetSource(BaseModel):
    Name: StrictStr | None = None
    Paths: list[StrictStr] | None = None
    CompressionType: StrictStr | None = None
    Exclusions: list[StrictStr] | None = None
    GroupSize: StrictStr | None = None
    GroupFiles: StrictStr | None = None
    Recurse: StrictBool | None = None
    MaxBand: StrictInt | None = None
    MaxFilesInBand: StrictInt | None = None
    AdditionalOptions: GlueS3DirectSourceAdditionalOptions | None = None
    OutputSchemas: list[GlueSchema] | None = None
