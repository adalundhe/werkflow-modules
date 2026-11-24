from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_stream_app_block_builder_app_block_association import AppStreamAppBlockBuilderAppBlockAssociation


class AppStreamAssociateAppBlockBuilderAppBlockResponse(BaseModel):
    AppBlockBuilderAppBlockAssociation: AppStreamAppBlockBuilderAppBlockAssociation | None = None
    ResponseMetadata: dict[str, Any] | None = None
