from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .batch_eks_container_detail import BatchEksContainerDetail
from .batch_eks_metadata import BatchEksMetadata
from .batch_eks_pod_security_context import BatchEksPodSecurityContext
from .batch_eks_volume import BatchEksVolume
from .batch_image_pull_secret import BatchImagePullSecret


class BatchEksPodPropertiesDetail(BaseModel):
    serviceAccountName: StrictStr | None = None
    hostNetwork: StrictBool | None = None
    dnsPolicy: StrictStr | None = None
    imagePullSecrets: list[BatchImagePullSecret] | None = None
    containers: list[BatchEksContainerDetail] | None = None
    initContainers: list[BatchEksContainerDetail] | None = None
    volumes: list[BatchEksVolume] | None = None
    podName: StrictStr | None = None
    nodeName: StrictStr | None = None
    metadata: BatchEksMetadata | None = None
    shareProcessNamespace: StrictBool | None = None
    securityContext: BatchEksPodSecurityContext | None = None
