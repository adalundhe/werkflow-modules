from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr
from .history_metadata_participant import HistoryMetadataParticipant


class HistoryMetadata(BaseModel):
    model_config = ConfigDict(extra="allow")

    activityDescription: StrictStr | None = None
    activityDescriptionKey: StrictStr | None = None
    actor: HistoryMetadataParticipant | None = None
    cause: HistoryMetadataParticipant | None = None
    description: StrictStr | None = None
    descriptionKey: StrictStr | None = None
    emailDescription: StrictStr | None = None
    emailDescriptionKey: StrictStr | None = None
    extraData: dict[StrictStr, StrictStr] | None = None
    generator: HistoryMetadataParticipant | None = None
    type: StrictStr | None = None
