from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .time_tracking_configuration import TimeTrackingConfiguration


class Configuration(BaseModel):
    attachmentsEnabled: StrictBool | None = None
    issueLinkingEnabled: StrictBool | None = None
    subTasksEnabled: StrictBool | None = None
    timeTrackingConfiguration: TimeTrackingConfiguration | None = None
    timeTrackingEnabled: StrictBool | None = None
    unassignedIssuesAllowed: StrictBool | None = None
    votingEnabled: StrictBool | None = None
    watchingEnabled: StrictBool | None = None
