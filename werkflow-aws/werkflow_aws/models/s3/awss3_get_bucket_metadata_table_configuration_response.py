from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .awss3_get_bucket_metadata_table_configuration_result import AWSS3GetBucketMetadataTableConfigurationResult


class AWSS3GetBucketMetadataTableConfigurationResponse(BaseModel):
    GetBucketMetadataTableConfigurationResult: AWSS3GetBucketMetadataTableConfigurationResult | None = None
    ResponseMetadata: dict[str, Any] | None = None
