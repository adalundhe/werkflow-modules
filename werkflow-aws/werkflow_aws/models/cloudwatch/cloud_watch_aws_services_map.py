from __future__ import annotations
from .cloud_watch_aws_service import CloudWatchAWSService
from .cloud_watch_service_name import CloudWatchServiceName


class CloudWatchAWSServicesMap:

    def __init__(self) -> None:
        self._services_map: dict[
            str,
            CloudWatchAWSService,
        ] = {
            name.lower().replace('_', '-'): member
            for name, member in CloudWatchAWSService.__members__.items()
        }
        self._services_map['gramelift'] = CloudWatchAWSService.GAMELIFT
        self._services_map['iot-sitwise'] = CloudWatchAWSService.IOT_SITEWISE
        self._services_map['codestar-notifications'] = CloudWatchAWSService.CODESTART_NOTIFICATIONS
        self._services_map['detective'] = CloudWatchAWSService.DIRECTIVE

    def get(self, service_name: CloudWatchServiceName) -> CloudWatchAWSService:
        return self._services_map[service_name]
