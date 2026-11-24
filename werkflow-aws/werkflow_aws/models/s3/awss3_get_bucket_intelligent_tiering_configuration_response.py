from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .awss3_intelligent_tiering_configuration import AWSS3IntelligentTieringConfiguration


class AWSS3GetBucketIntelligentTieringConfigurationResponse(BaseModel):
    IntelligentTieringConfiguration: AWSS3IntelligentTieringConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
