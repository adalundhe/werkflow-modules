from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_tagged_resource import RedshiftTaggedResource


class RedshiftDescribeTagsResponse(BaseModel):
    TaggedResources: list[RedshiftTaggedResource] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
