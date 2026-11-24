from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_stream_app_block_builder_app_block_association import AppStreamAppBlockBuilderAppBlockAssociation


class AppStreamDescribeAppBlockBuilderAppBlockAssociationsResponse(BaseModel):
    AppBlockBuilderAppBlockAssociations: list[AppStreamAppBlockBuilderAppBlockAssociation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
