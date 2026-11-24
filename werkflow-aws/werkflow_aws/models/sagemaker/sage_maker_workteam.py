from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_member_definition import SageMakerMemberDefinition
from .sage_maker_notification_configuration import SageMakerNotificationConfiguration
from .sage_maker_worker_access_configuration import SageMakerWorkerAccessConfiguration


class SageMakerWorkteam(BaseModel):
    WorkteamName: StrictStr | None = None
    MemberDefinitions: list[SageMakerMemberDefinition] | None = None
    WorkteamArn: StrictStr | None = None
    WorkforceArn: StrictStr | None = None
    ProductListingIds: list[StrictStr] | None = None
    Description: StrictStr | None = None
    SubDomain: StrictStr | None = None
    CreateDate: datetime.datetime | StrictStr | None = None
    LastUpdatedDate: datetime.datetime | StrictStr | None = None
    NotificationConfiguration: SageMakerNotificationConfiguration | None = None
    WorkerAccessConfiguration: SageMakerWorkerAccessConfiguration | None = None
