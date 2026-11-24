from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cognito_sync_record_patch import CognitoSyncRecordPatch


class CognitoSyncUpdateRecordsRequest(BaseModel):
    IdentityPoolId: StrictStr
    IdentityId: StrictStr
    DatasetName: StrictStr
    SyncSessionToken: StrictStr
    DeviceId: StrictStr | None = None
    RecordPatches: list[CognitoSyncRecordPatch] | None = None
    ClientContext: StrictStr | None = None
