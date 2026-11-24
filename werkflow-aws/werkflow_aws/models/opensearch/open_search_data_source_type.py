from __future__ import annotations
from pydantic import BaseModel
from .open_search_s3_glue_data_catalog import OpenSearchS3GlueDataCatalog


class OpenSearchDataSourceType(BaseModel):
    S3GlueDataCatalog: OpenSearchS3GlueDataCatalog | None = None
