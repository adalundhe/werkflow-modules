from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecr_image_identifier import ECRImageIdentifier
from .ecr_image_replication_status import ECRImageReplicationStatus


class ECRDescribeImageReplicationStatusResponse(BaseModel):
    repositoryName: StrictStr | None = None
    imageId: ECRImageIdentifier | None = None
    replicationStatuses: list[ECRImageReplicationStatus] | None = None
    ResponseMetadata: dict[str, Any] | None = None
