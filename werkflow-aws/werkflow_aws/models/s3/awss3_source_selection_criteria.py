from __future__ import annotations
from pydantic import BaseModel
from .awss3_replica_modifications import AWSS3ReplicaModifications
from .awss3_sse_kms_encrypted_objects import AWSS3SseKmsEncryptedObjects


class AWSS3SourceSelectionCriteria(BaseModel):
    SseKmsEncryptedObjects: AWSS3SseKmsEncryptedObjects | None = None
    ReplicaModifications: AWSS3ReplicaModifications | None = None
