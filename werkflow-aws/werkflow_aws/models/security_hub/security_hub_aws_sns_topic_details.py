from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_sns_topic_subscription import SecurityHubAwsSnsTopicSubscription


class SecurityHubAwsSnsTopicDetails(BaseModel):
    KmsMasterKeyId: StrictStr | None = None
    Subscription: list[SecurityHubAwsSnsTopicSubscription] | None = None
    TopicName: StrictStr | None = None
    Owner: StrictStr | None = None
    SqsSuccessFeedbackRoleArn: StrictStr | None = None
    SqsFailureFeedbackRoleArn: StrictStr | None = None
    ApplicationSuccessFeedbackRoleArn: StrictStr | None = None
    FirehoseSuccessFeedbackRoleArn: StrictStr | None = None
    FirehoseFailureFeedbackRoleArn: StrictStr | None = None
    HttpSuccessFeedbackRoleArn: StrictStr | None = None
    HttpFailureFeedbackRoleArn: StrictStr | None = None
