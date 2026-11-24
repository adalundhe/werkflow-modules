from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_stream_user_stack_association import AppStreamUserStackAssociation


class AppStreamDescribeUserStackAssociationsResponse(BaseModel):
    UserStackAssociations: list[AppStreamUserStackAssociation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
