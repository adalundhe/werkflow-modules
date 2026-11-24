from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .f_sx_create_snapmirror_destination import FSxCreateSnapmirrorDestination
from .f_sx_create_snapmirror_source import FSxCreateSnapmirrorSource
from .f_sx_tag import FSxTag


class FSxCreateSnapmirrorRelationshipRequest(BaseModel):
    Source: FSxCreateSnapmirrorSource
    Destination: FSxCreateSnapmirrorDestination
    ClientRequestToken: StrictStr | None = None
    PolicyId: StrictStr | None = None
    TransferSchedule: StrictStr | None = None
    ThrottleInKbps: StrictInt | None = None
    Tags: list[FSxTag] | None = None
