from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .awss3_abort_incomplete_multipart_upload import AWSS3AbortIncompleteMultipartUpload
from .awss3_lifecycle_expiration import AWSS3LifecycleExpiration
from .awss3_lifecycle_rule_filter import AWSS3LifecycleRuleFilter
from .awss3_noncurrent_version_expiration import AWSS3NoncurrentVersionExpiration
from .awss3_noncurrent_version_transition import AWSS3NoncurrentVersionTransition
from .awss3_transition import AWSS3Transition


class AWSS3LifecycleRule(BaseModel):
    Expiration: AWSS3LifecycleExpiration | None = None
    ID: StrictStr | None = None
    Prefix: StrictStr | None = None
    Filter: AWSS3LifecycleRuleFilter | None = None
    Status: Literal['Enabled', 'Disabled'] | None = None
    Transitions: list[AWSS3Transition] | None = None
    NoncurrentVersionTransitions: list[AWSS3NoncurrentVersionTransition] | None = None
    NoncurrentVersionExpiration: AWSS3NoncurrentVersionExpiration | None = None
    AbortIncompleteMultipartUpload: AWSS3AbortIncompleteMultipartUpload | None = None
