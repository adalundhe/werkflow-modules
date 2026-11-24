from __future__ import annotations
from typing import Literal


SQSMessageSystemAttributeName = Literal[
    'All',
    'SenderId',
    'SentTimestamp',
    'ApproximateReceiveCount',
    'ApproximateFirstReceiveTimestamp',
    'SequenceNumber',
    'MessageDeduplicationId',
    'MessageGroupId',
    'AWSTraceHeader',
    'DeadLetterQueueSourceArn',
]
