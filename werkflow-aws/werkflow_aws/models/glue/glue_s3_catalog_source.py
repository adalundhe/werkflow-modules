from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_s3_source_additional_options import GlueS3SourceAdditionalOptions


class GlueS3CatalogSource(BaseModel):
    Name: StrictStr | None = None
    Database: StrictStr | None = None
    Table: StrictStr | None = None
    PartitionPredicate: StrictStr | None = None
    AdditionalOptions: GlueS3SourceAdditionalOptions | None = None
