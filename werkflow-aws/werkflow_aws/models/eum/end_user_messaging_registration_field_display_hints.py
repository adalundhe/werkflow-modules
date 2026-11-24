from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .end_user_messaging_select_option_description import EndUserMessagingSelectOptionDescription


class EndUserMessagingRegistrationFieldDisplayHints(BaseModel):
    Title: StrictStr | None = None
    ShortDescription: StrictStr | None = None
    LongDescription: StrictStr | None = None
    DocumentationTitle: StrictStr | None = None
    DocumentationLink: StrictStr | None = None
    SelectOptionDescriptions: list[EndUserMessagingSelectOptionDescription] | None = None
    TextValidationDescription: StrictStr | None = None
    ExampleTextValue: StrictStr | None = None
