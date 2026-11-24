from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .batch_eks_empty_dir import BatchEksEmptyDir
from .batch_eks_host_path import BatchEksHostPath
from .batch_eks_persistent_volume_claim import BatchEksPersistentVolumeClaim
from .batch_eks_secret import BatchEksSecret


class BatchEksVolume(BaseModel):
    name: StrictStr | None = None
    hostPath: BatchEksHostPath | None = None
    emptyDir: BatchEksEmptyDir | None = None
    secret: BatchEksSecret | None = None
    persistentVolumeClaim: BatchEksPersistentVolumeClaim | None = None
