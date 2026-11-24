from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .emr_block_public_access_configuration import EMRBlockPublicAccessConfiguration
from .emr_block_public_access_configuration_metadata import EMRBlockPublicAccessConfigurationMetadata


class EMRGetBlockPublicAccessConfigurationResponse(BaseModel):
    BlockPublicAccessConfiguration: EMRBlockPublicAccessConfiguration | None = None
    BlockPublicAccessConfigurationMetadata: EMRBlockPublicAccessConfigurationMetadata | None = None
    ResponseMetadata: dict[str, Any] | None = None
