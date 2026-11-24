from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .msk_topic_reassignment_info import MSKTopicReassignmentInfo


class MSKListTopicReassignmentsResponse(BaseModel):
    NextToken: StrictStr | None = None
    Reassignments: list[MSKTopicReassignmentInfo] | None = None
    ResponseMetadata: dict[str, Any] | None = None
