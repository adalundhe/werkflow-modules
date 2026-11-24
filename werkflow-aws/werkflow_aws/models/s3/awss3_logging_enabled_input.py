from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .awss3_target_grant_input import AWSS3TargetGrantInput
from .awss3_target_object_key_format_input import AWSS3TargetObjectKeyFormatInput


class AWSS3LoggingEnabledInput(BaseModel):
    TargetBucket: StrictStr
    TargetPrefix: StrictStr
    TargetGrants: list[AWSS3TargetGrantInput] | None = None
    TargetObjectKeyFormat: AWSS3TargetObjectKeyFormatInput | None = None
