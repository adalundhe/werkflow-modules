from __future__ import annotations
from pydantic import BaseModel
from .custom_field_payload import CustomFieldPayload
from .field_layout_payload import FieldLayoutPayload
from .field_layout_scheme_payload import FieldLayoutSchemePayload
from .field_scheme_payload import FieldSchemePayload
from .issue_layout_payload import IssueLayoutPayload
from .issue_type_screen_scheme_payload import IssueTypeScreenSchemePayload
from .screen_payload import ScreenPayload
from .screen_scheme_payload import ScreenSchemePayload


class FieldCapabilityPayload(BaseModel):
    customFieldDefinitions: list[CustomFieldPayload] | None = None
    fieldLayoutScheme: FieldLayoutSchemePayload | None = None
    fieldLayouts: list[FieldLayoutPayload] | None = None
    fieldScheme: FieldSchemePayload | None = None
    issueLayouts: list[IssueLayoutPayload] | None = None
    issueTypeScreenScheme: IssueTypeScreenSchemePayload | None = None
    screenScheme: list[ScreenSchemePayload] | None = None
    screens: list[ScreenPayload] | None = None
