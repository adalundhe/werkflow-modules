from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .awss3_get_bucket_metadata_configuration_result import AWSS3GetBucketMetadataConfigurationResult


class AWSS3GetBucketMetadataConfigurationResponse(BaseModel):
    GetBucketMetadataConfigurationResult: AWSS3GetBucketMetadataConfigurationResult | None = None
    ResponseMetadata: dict[str, Any] | None = None
