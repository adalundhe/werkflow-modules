from __future__ import annotations
from pydantic import BaseModel
from .ses_contact_list_destination import SESContactListDestination
from .ses_suppression_list_destination import SESSuppressionListDestination


class SESImportDestination(BaseModel):
    SuppressionListDestination: SESSuppressionListDestination | None = None
    ContactListDestination: SESContactListDestination | None = None
