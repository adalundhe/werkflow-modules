from __future__ import annotations
from typing import Literal


SageMakerSecondaryStatus = Literal[
    'Starting',
    'LaunchingMLInstances',
    'PreparingTrainingStack',
    'Downloading',
    'DownloadingTrainingImage',
    'Training',
    'Uploading',
    'Stopping',
    'Stopped',
    'MaxRuntimeExceeded',
    'Completed',
    'Failed',
    'Interrupted',
    'MaxWaitTimeExceeded',
    'Updating',
    'Restarting',
    'Pending',
]
