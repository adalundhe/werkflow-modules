from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_s3_direct_source_additional_options import GlueS3DirectSourceAdditionalOptions
from .glue_schema import GlueSchema


class GlueS3HudiSource(BaseModel):
    Name: StrictStr | None = None
    Paths: list[StrictStr] | None = None
    AdditionalHudiOptions: dict[StrictStr, StrictStr] | None = None
    AdditionalOptions: GlueS3DirectSourceAdditionalOptions | None = None
    OutputSchemas: list[GlueSchema] | None = None
