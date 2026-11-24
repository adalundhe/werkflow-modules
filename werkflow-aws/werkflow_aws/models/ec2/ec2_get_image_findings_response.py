from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_image_finding import EC2ImageFinding


class EC2GetImageFindingsResponse(BaseModel):
    ImageFindings: list[EC2ImageFinding] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
