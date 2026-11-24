from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .glue_s3_direct_source_additional_options import GlueS3DirectSourceAdditionalOptions
from .glue_schema import GlueSchema


class GlueS3CsvSource(BaseModel):
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
    Separator: StrictStr | None = None
    Escaper: StrictStr | None = None
    QuoteChar: StrictStr | None = None
    Multiline: StrictBool | None = None
    WithHeader: StrictBool | None = None
    WriteHeader: StrictBool | None = None
    SkipFirst: StrictBool | None = None
    OptimizePerformance: StrictBool | None = None
    OutputSchemas: list[GlueSchema] | None = None
