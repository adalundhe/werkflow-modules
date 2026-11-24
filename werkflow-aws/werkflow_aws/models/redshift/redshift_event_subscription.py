from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .redshift_tag import RedshiftTag


class RedshiftEventSubscription(BaseModel):
    CustomerAwsId: StrictStr | None = None
    CustSubscriptionId: StrictStr | None = None
    SnsTopicArn: StrictStr | None = None
    Status: StrictStr | None = None
    SubscriptionCreationTime: datetime.datetime | StrictStr | None = None
    SourceType: StrictStr | None = None
    SourceIdsList: list[StrictStr] | None = None
    EventCategoriesList: list[StrictStr] | None = None
    Severity: StrictStr | None = None
    Enabled: StrictBool | None = None
    Tags: list[RedshiftTag] | None = None
