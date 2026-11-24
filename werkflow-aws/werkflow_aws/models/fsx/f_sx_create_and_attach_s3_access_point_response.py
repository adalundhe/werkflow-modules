from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .f_sx_s3_access_point_attachment import FSxS3AccessPointAttachment


class FSxCreateAndAttachS3AccessPointResponse(BaseModel):
    S3AccessPointAttachment: FSxS3AccessPointAttachment | None = None
    ResponseMetadata: dict[str, Any] | None = None
