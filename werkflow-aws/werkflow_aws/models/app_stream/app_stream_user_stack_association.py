from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AppStreamUserStackAssociation(BaseModel):
    StackName: StrictStr | None = None
    UserName: StrictStr | None = None
    AuthenticationType: StrictStr | None = None
    SendEmailNotification: StrictBool | None = None
