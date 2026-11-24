from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .awss3_intelligent_tiering_configuration import AWSS3IntelligentTieringConfiguration


class AWSS3PutBucketIntelligentTieringConfigurationRequest(BaseModel):
    Bucket: StrictStr
    Id: StrictStr
    IntelligentTieringConfiguration: AWSS3IntelligentTieringConfiguration
    ExpectedBucketOwner: StrictStr | None = None
