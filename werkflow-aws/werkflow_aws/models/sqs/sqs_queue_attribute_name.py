from __future__ import annotations
from typing import Literal


SQSQueueAttributeName = Literal[
    'All',
    'Policy',
    'VisibilityTimeout',
    'MaximumMessageSize',
    'MessageRetentionPeriod',
    'ApproximateNumberOfMessages',
    'ApproximateNumberOfMessagesNotVisible',
    'CreatedTimestamp',
    'LastModifiedTimestamp',
    'QueueArn',
    'ApproximateNumberOfMessagesDelayed',
    'DelaySeconds',
    'ReceiveMessageWaitTimeSeconds',
    'RedrivePolicy',
    'FifoQueue',
    'ContentBasedDeduplication',
    'KmsMasterKeyId',
    'KmsDataKeyReusePeriodSeconds',
    'DeduplicationScope',
    'FifoThroughputLimit',
    'RedriveAllowPolicy',
    'SqsManagedSseEnabled',
]
