from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .awss3_abort_incomplete_multipart_upload_input import AWSS3AbortIncompleteMultipartUploadInput
from .awss3_lifecycle_expiration_input import AWSS3LifecycleExpirationInput
from .awss3_lifecycle_rule_filter_input import AWSS3LifecycleRuleFilterInput
from .awss3_noncurrent_version_expiration_input import AWSS3NoncurrentVersionExpirationInput
from .awss3_noncurrent_version_transition_input import AWSS3NoncurrentVersionTransitionInput
from .awss3_transition_input import AWSS3TransitionInput


class AWSS3LifecycleRuleInput(BaseModel):
    Status: Literal['Enabled', 'Disabled']
    Expiration: AWSS3LifecycleExpirationInput | None = None
    ID: StrictStr | None = None
    Prefix: StrictStr | None = None
    Filter: AWSS3LifecycleRuleFilterInput | None = None
    Transitions: list[AWSS3TransitionInput] | None = None
    NoncurrentVersionTransitions: list[AWSS3NoncurrentVersionTransitionInput] | None = None
    NoncurrentVersionExpiration: AWSS3NoncurrentVersionExpirationInput | None = None
    AbortIncompleteMultipartUpload: AWSS3AbortIncompleteMultipartUploadInput | None = None
