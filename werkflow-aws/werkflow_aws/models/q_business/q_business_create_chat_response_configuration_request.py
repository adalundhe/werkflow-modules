from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .q_business_response_configuration import QBusinessResponseConfiguration
from .q_business_tag import QBusinessTag


class QBusinessCreateChatResponseConfigurationRequest(BaseModel):
    applicationId: StrictStr
    displayName: StrictStr
    responseConfigurations: dict[Literal['ALL'], QBusinessResponseConfiguration]
    clientToken: StrictStr | None = None
    tags: list[QBusinessTag] | None = None
