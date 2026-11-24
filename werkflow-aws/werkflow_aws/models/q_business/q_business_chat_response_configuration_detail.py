from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .q_business_error_detail import QBusinessErrorDetail
from .q_business_response_configuration import QBusinessResponseConfiguration


class QBusinessChatResponseConfigurationDetail(BaseModel):
    responseConfigurations: dict[StrictStr, QBusinessResponseConfiguration] | None = None
    responseConfigurationSummary: StrictStr | None = None
    status: StrictStr | None = None
    error: QBusinessErrorDetail | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
