from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictStr
from .entity_property import EntityProperty
from .field_update_operation import FieldUpdateOperation
from .history_metadata import HistoryMetadata
from .issue_transition import IssueTransition


class IssueUpdateDetails(BaseModel):
    model_config = ConfigDict(extra="allow")

    fields: dict[StrictStr, Any] | None = None
    historyMetadata: HistoryMetadata | None = None
    properties: list[EntityProperty] | None = None
    transition: IssueTransition | None = None
    update: dict[StrictStr, list[FieldUpdateOperation]] | None = None
