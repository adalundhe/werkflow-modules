from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .awss3_intelligent_tiering_configuration import AWSS3IntelligentTieringConfiguration


class AWSS3ListBucketIntelligentTieringConfigurationsResponse(BaseModel):
    IsTruncated: StrictBool | None = None
    ContinuationToken: StrictStr | None = None
    NextContinuationToken: StrictStr | None = None
    IntelligentTieringConfigurationList: list[AWSS3IntelligentTieringConfiguration] | None = None
    ResponseMetadata: dict[str, Any] | None = None
