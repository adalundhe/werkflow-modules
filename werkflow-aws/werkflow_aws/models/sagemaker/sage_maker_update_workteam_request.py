from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_member_definition import SageMakerMemberDefinition
from .sage_maker_notification_configuration import SageMakerNotificationConfiguration
from .sage_maker_worker_access_configuration import SageMakerWorkerAccessConfiguration


class SageMakerUpdateWorkteamRequest(BaseModel):
    WorkteamName: StrictStr
    MemberDefinitions: list[SageMakerMemberDefinition] | None = None
    Description: StrictStr | None = None
    NotificationConfiguration: SageMakerNotificationConfiguration | None = None
    WorkerAccessConfiguration: SageMakerWorkerAccessConfiguration | None = None
