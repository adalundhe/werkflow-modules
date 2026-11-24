from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .device_farm_trial_minutes import DeviceFarmTrialMinutes


class DeviceFarmAccountSettings(BaseModel):
    awsAccountNumber: StrictStr | None = None
    unmeteredDevices: dict[StrictStr, StrictInt] | None = None
    unmeteredRemoteAccessDevices: dict[StrictStr, StrictInt] | None = None
    maxJobTimeoutMinutes: StrictInt | None = None
    trialMinutes: DeviceFarmTrialMinutes | None = None
    maxSlots: dict[StrictStr, StrictInt] | None = None
    defaultJobTimeoutMinutes: StrictInt | None = None
    skipAppResign: StrictBool | None = None
