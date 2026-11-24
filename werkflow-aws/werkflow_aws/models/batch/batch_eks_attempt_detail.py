from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .batch_eks_attempt_container_detail import BatchEksAttemptContainerDetail


class BatchEksAttemptDetail(BaseModel):
    containers: list[BatchEksAttemptContainerDetail] | None = None
    initContainers: list[BatchEksAttemptContainerDetail] | None = None
    eksClusterArn: StrictStr | None = None
    podName: StrictStr | None = None
    podNamespace: StrictStr | None = None
    nodeName: StrictStr | None = None
    startedAt: StrictInt | None = None
    stoppedAt: StrictInt | None = None
    statusReason: StrictStr | None = None
