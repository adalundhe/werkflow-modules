from __future__ import annotations
from pydantic import BaseModel
from .app_stream_user_stack_association import AppStreamUserStackAssociation


class AppStreamBatchDisassociateUserStackRequest(BaseModel):
    UserStackAssociations: list[AppStreamUserStackAssociation]
