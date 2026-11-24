from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .directory_service_event_topic import DirectoryServiceEventTopic


class DirectoryServiceDescribeEventTopicsResponse(BaseModel):
    EventTopics: list[DirectoryServiceEventTopic] | None = None
    ResponseMetadata: dict[str, Any] | None = None
