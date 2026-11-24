from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .f_sx_s3_access_point_attachment import FSxS3AccessPointAttachment


class FSxDescribeS3AccessPointAttachmentsResponse(BaseModel):
    S3AccessPointAttachments: list[FSxS3AccessPointAttachment] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
