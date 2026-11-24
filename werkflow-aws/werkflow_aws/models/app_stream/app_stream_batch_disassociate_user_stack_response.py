from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_stream_user_stack_association_error import AppStreamUserStackAssociationError


class AppStreamBatchDisassociateUserStackResponse(BaseModel):
    errors: list[AppStreamUserStackAssociationError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
