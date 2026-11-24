from __future__ import annotations
from pydantic import BaseModel
from .io_t_add_things_to_thing_group_params import IoTAddThingsToThingGroupParams
from .io_t_enable_io_t_logging_params import IoTEnableIoTLoggingParams
from .io_t_publish_finding_to_sns_params import IoTPublishFindingToSnsParams
from .io_t_replace_default_policy_version_params import IoTReplaceDefaultPolicyVersionParams
from .io_t_update_ca_certificate_params import IoTUpdateCACertificateParams
from .io_t_update_device_certificate_params import IoTUpdateDeviceCertificateParams


class IoTMitigationActionParams(BaseModel):
    updateDeviceCertificateParams: IoTUpdateDeviceCertificateParams | None = None
    updateCACertificateParams: IoTUpdateCACertificateParams | None = None
    addThingsToThingGroupParams: IoTAddThingsToThingGroupParams | None = None
    replaceDefaultPolicyVersionParams: IoTReplaceDefaultPolicyVersionParams | None = None
    enableIoTLoggingParams: IoTEnableIoTLoggingParams | None = None
    publishFindingToSnsParams: IoTPublishFindingToSnsParams | None = None
