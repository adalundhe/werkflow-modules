from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_image_ancestry_entry import EC2ImageAncestryEntry


class EC2GetImageAncestryResponse(BaseModel):
    ImageAncestryEntries: list[EC2ImageAncestryEntry] | None = None
    ResponseMetadata: dict[str, Any] | None = None
