from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .q_business_action_execution import QBusinessActionExecution
from .q_business_action_review import QBusinessActionReview
from .q_business_attachment_output import QBusinessAttachmentOutput
from .q_business_source_attribution import QBusinessSourceAttribution


class QBusinessMessage(BaseModel):
    messageId: StrictStr | None = None
    body: StrictStr | None = None
    time: datetime.datetime | StrictStr | None = None
    type: StrictStr | None = None
    attachments: list[QBusinessAttachmentOutput] | None = None
    sourceAttribution: list[QBusinessSourceAttribution] | None = None
    actionReview: QBusinessActionReview | None = None
    actionExecution: QBusinessActionExecution | None = None
