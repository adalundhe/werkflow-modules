from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .q_business_response_configuration import QBusinessResponseConfiguration


class QBusinessUpdateChatResponseConfigurationRequest(BaseModel):
    applicationId: StrictStr
    chatResponseConfigurationId: StrictStr
    responseConfigurations: dict[Literal['ALL'], QBusinessResponseConfiguration]
    displayName: StrictStr | None = None
    clientToken: StrictStr | None = None
