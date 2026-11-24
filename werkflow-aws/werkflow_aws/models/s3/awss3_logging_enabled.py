from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .awss3_target_grant import AWSS3TargetGrant
from .awss3_target_object_key_format import AWSS3TargetObjectKeyFormat


class AWSS3LoggingEnabled(BaseModel):
    TargetBucket: StrictStr | None = None
    TargetGrants: list[AWSS3TargetGrant] | None = None
    TargetPrefix: StrictStr | None = None
    TargetObjectKeyFormat: AWSS3TargetObjectKeyFormat | None = None
