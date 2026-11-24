from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .end_user_messaging_template_variable_metadata import EndUserMessagingTemplateVariableMetadata


class EndUserMessagingNotifyTemplateInformation(BaseModel):
    TemplateId: StrictStr | None = None
    Version: StrictInt | None = None
    TemplateType: StrictStr | None = None
    Channels: list[StrictStr] | None = None
    TierAccess: list[StrictStr] | None = None
    Status: StrictStr | None = None
    SupportedCountries: list[StrictStr] | None = None
    LanguageCode: StrictStr | None = None
    Content: StrictStr | None = None
    Variables: dict[StrictStr, EndUserMessagingTemplateVariableMetadata] | None = None
    SupportedVoiceIds: list[StrictStr] | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
