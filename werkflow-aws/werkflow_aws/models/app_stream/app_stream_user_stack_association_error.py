from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_stream_user_stack_association import AppStreamUserStackAssociation


class AppStreamUserStackAssociationError(BaseModel):
    UserStackAssociation: AppStreamUserStackAssociation | None = None
    ErrorCode: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
