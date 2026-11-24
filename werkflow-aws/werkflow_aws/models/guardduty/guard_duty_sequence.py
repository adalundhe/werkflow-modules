from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_actor import GuardDutyActor
from .guard_duty_indicator import GuardDutyIndicator
from .guard_duty_network_endpoint import GuardDutyNetworkEndpoint
from .guard_duty_resource_v2 import GuardDutyResourceV2
from .guard_duty_signal import GuardDutySignal


class GuardDutySequence(BaseModel):
    Uid: StrictStr | None = None
    Description: StrictStr | None = None
    Actors: list[GuardDutyActor] | None = None
    Resources: list[GuardDutyResourceV2] | None = None
    Endpoints: list[GuardDutyNetworkEndpoint] | None = None
    Signals: list[GuardDutySignal] | None = None
    SequenceIndicators: list[GuardDutyIndicator] | None = None
    AdditionalSequenceTypes: list[StrictStr] | None = None
