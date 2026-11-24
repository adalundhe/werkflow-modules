from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectEvaluationContactParticipant(BaseModel):
    ContactParticipantRole: StrictStr | None = None
    ContactParticipantId: StrictStr | None = None
