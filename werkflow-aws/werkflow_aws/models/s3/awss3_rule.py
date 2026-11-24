from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .awss3_abort_incomplete_multipart_upload_model import AWSS3AbortIncompleteMultipartUploadModel
from .awss3_lifecycle_expiration_model import AWSS3LifecycleExpirationModel
from .awss3_noncurrent_version_expiration_model import AWSS3NoncurrentVersionExpirationModel
from .awss3_noncurrent_version_transition_model import AWSS3NoncurrentVersionTransitionModel
from .awss3_transition_model import AWSS3TransitionModel


class AWSS3Rule(BaseModel):
    Expiration: AWSS3LifecycleExpirationModel | None = None
    ID: StrictStr | None = None
    Prefix: StrictStr | None = None
    Status: StrictStr | None = None
    Transition: AWSS3TransitionModel | None = None
    NoncurrentVersionTransition: AWSS3NoncurrentVersionTransitionModel | None = None
    NoncurrentVersionExpiration: AWSS3NoncurrentVersionExpirationModel | None = None
    AbortIncompleteMultipartUpload: AWSS3AbortIncompleteMultipartUploadModel | None = None
