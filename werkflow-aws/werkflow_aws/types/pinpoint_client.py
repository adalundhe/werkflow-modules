from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class PinpointClient(ABC):

    @abstractmethod
    def create_app(
        self,
        *,
        CreateApplicationRequest: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_campaign(
        self,
        *,
        ApplicationId: str,
        WriteCampaignRequest: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_email_template(
        self,
        *,
        EmailTemplateRequest: dict[str, Any],
        TemplateName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_export_job(
        self,
        *,
        ApplicationId: str,
        ExportJobRequest: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_import_job(
        self,
        *,
        ApplicationId: str,
        ImportJobRequest: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_in_app_template(
        self,
        *,
        InAppTemplateRequest: dict[str, Any],
        TemplateName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_journey(
        self,
        *,
        ApplicationId: str,
        WriteJourneyRequest: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_push_template(
        self,
        *,
        PushNotificationTemplateRequest: dict[str, Any],
        TemplateName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_recommender_configuration(
        self,
        *,
        CreateRecommenderConfiguration: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_segment(
        self,
        *,
        ApplicationId: str,
        WriteSegmentRequest: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_sms_template(
        self,
        *,
        SMSTemplateRequest: dict[str, Any],
        TemplateName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_voice_template(
        self,
        *,
        TemplateName: str,
        VoiceTemplateRequest: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_adm_channel(
        self,
        *,
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_apns_channel(
        self,
        *,
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_apns_sandbox_channel(
        self,
        *,
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_apns_voip_channel(
        self,
        *,
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_apns_voip_sandbox_channel(
        self,
        *,
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_app(
        self,
        *,
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_baidu_channel(
        self,
        *,
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_campaign(
        self,
        *,
        ApplicationId: str,
        CampaignId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_email_channel(
        self,
        *,
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_email_template(
        self,
        *,
        TemplateName: str,
        Version: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_endpoint(
        self,
        *,
        ApplicationId: str,
        EndpointId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_event_stream(
        self,
        *,
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_gcm_channel(
        self,
        *,
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_in_app_template(
        self,
        *,
        TemplateName: str,
        Version: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_journey(
        self,
        *,
        ApplicationId: str,
        JourneyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_push_template(
        self,
        *,
        TemplateName: str,
        Version: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_recommender_configuration(
        self,
        *,
        RecommenderId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_segment(
        self,
        *,
        ApplicationId: str,
        SegmentId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_sms_channel(
        self,
        *,
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_sms_template(
        self,
        *,
        TemplateName: str,
        Version: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_user_endpoints(
        self,
        *,
        ApplicationId: str,
        UserId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_voice_channel(
        self,
        *,
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_voice_template(
        self,
        *,
        TemplateName: str,
        Version: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_adm_channel(
        self,
        *,
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_apns_channel(
        self,
        *,
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_apns_sandbox_channel(
        self,
        *,
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_apns_voip_channel(
        self,
        *,
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_apns_voip_sandbox_channel(
        self,
        *,
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_app(
        self,
        *,
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_application_date_range_kpi(
        self,
        *,
        ApplicationId: str,
        KpiName: str,
        EndTime: datetime.datetime | str | None = None,
        NextToken: str | None = None,
        PageSize: str | None = None,
        StartTime: datetime.datetime | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_application_settings(
        self,
        *,
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_apps(
        self,
        *,
        PageSize: str | None = None,
        Token: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_baidu_channel(
        self,
        *,
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_campaign(
        self,
        *,
        ApplicationId: str,
        CampaignId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_campaign_activities(
        self,
        *,
        ApplicationId: str,
        CampaignId: str,
        PageSize: str | None = None,
        Token: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_campaign_date_range_kpi(
        self,
        *,
        ApplicationId: str,
        CampaignId: str,
        KpiName: str,
        EndTime: datetime.datetime | str | None = None,
        NextToken: str | None = None,
        PageSize: str | None = None,
        StartTime: datetime.datetime | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_campaign_version(
        self,
        *,
        ApplicationId: str,
        CampaignId: str,
        Version: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_campaign_versions(
        self,
        *,
        ApplicationId: str,
        CampaignId: str,
        PageSize: str | None = None,
        Token: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_campaigns(
        self,
        *,
        ApplicationId: str,
        PageSize: str | None = None,
        Token: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_channels(
        self,
        *,
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_email_channel(
        self,
        *,
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_email_template(
        self,
        *,
        TemplateName: str,
        Version: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_endpoint(
        self,
        *,
        ApplicationId: str,
        EndpointId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_event_stream(
        self,
        *,
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_export_job(
        self,
        *,
        ApplicationId: str,
        JobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_export_jobs(
        self,
        *,
        ApplicationId: str,
        PageSize: str | None = None,
        Token: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_gcm_channel(
        self,
        *,
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_import_job(
        self,
        *,
        ApplicationId: str,
        JobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_import_jobs(
        self,
        *,
        ApplicationId: str,
        PageSize: str | None = None,
        Token: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_in_app_messages(
        self,
        *,
        ApplicationId: str,
        EndpointId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_in_app_template(
        self,
        *,
        TemplateName: str,
        Version: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_journey(
        self,
        *,
        ApplicationId: str,
        JourneyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_journey_date_range_kpi(
        self,
        *,
        ApplicationId: str,
        JourneyId: str,
        KpiName: str,
        EndTime: datetime.datetime | str | None = None,
        NextToken: str | None = None,
        PageSize: str | None = None,
        StartTime: datetime.datetime | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_journey_execution_activity_metrics(
        self,
        *,
        ApplicationId: str,
        JourneyActivityId: str,
        JourneyId: str,
        NextToken: str | None = None,
        PageSize: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_journey_execution_metrics(
        self,
        *,
        ApplicationId: str,
        JourneyId: str,
        NextToken: str | None = None,
        PageSize: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_journey_run_execution_activity_metrics(
        self,
        *,
        ApplicationId: str,
        JourneyActivityId: str,
        JourneyId: str,
        RunId: str,
        NextToken: str | None = None,
        PageSize: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_journey_run_execution_metrics(
        self,
        *,
        ApplicationId: str,
        JourneyId: str,
        RunId: str,
        NextToken: str | None = None,
        PageSize: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_journey_runs(
        self,
        *,
        ApplicationId: str,
        JourneyId: str,
        PageSize: str | None = None,
        Token: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_push_template(
        self,
        *,
        TemplateName: str,
        Version: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_recommender_configuration(
        self,
        *,
        RecommenderId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_recommender_configurations(
        self,
        *,
        PageSize: str | None = None,
        Token: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_segment(
        self,
        *,
        ApplicationId: str,
        SegmentId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_segment_export_jobs(
        self,
        *,
        ApplicationId: str,
        SegmentId: str,
        PageSize: str | None = None,
        Token: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_segment_import_jobs(
        self,
        *,
        ApplicationId: str,
        SegmentId: str,
        PageSize: str | None = None,
        Token: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_segment_version(
        self,
        *,
        ApplicationId: str,
        SegmentId: str,
        Version: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_segment_versions(
        self,
        *,
        ApplicationId: str,
        SegmentId: str,
        PageSize: str | None = None,
        Token: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_segments(
        self,
        *,
        ApplicationId: str,
        PageSize: str | None = None,
        Token: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_sms_channel(
        self,
        *,
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_sms_template(
        self,
        *,
        TemplateName: str,
        Version: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_user_endpoints(
        self,
        *,
        ApplicationId: str,
        UserId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_voice_channel(
        self,
        *,
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_voice_template(
        self,
        *,
        TemplateName: str,
        Version: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_journeys(
        self,
        *,
        ApplicationId: str,
        PageSize: str | None = None,
        Token: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_template_versions(
        self,
        *,
        TemplateName: str,
        TemplateType: str,
        NextToken: str | None = None,
        PageSize: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_templates(
        self,
        *,
        NextToken: str | None = None,
        PageSize: str | None = None,
        Prefix: str | None = None,
        TemplateType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def phone_number_validate(
        self,
        *,
        NumberValidateRequest: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_event_stream(
        self,
        *,
        ApplicationId: str,
        WriteEventStream: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_events(
        self,
        *,
        ApplicationId: str,
        EventsRequest: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_attributes(
        self,
        *,
        ApplicationId: str,
        AttributeType: str,
        UpdateAttributesRequest: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_messages(
        self,
        *,
        ApplicationId: str,
        MessageRequest: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_otp_message(
        self,
        *,
        ApplicationId: str,
        SendOTPMessageRequestParameters: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_users_messages(
        self,
        *,
        ApplicationId: str,
        SendUsersMessageRequest: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        ResourceArn: str,
        TagsModel: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        ResourceArn: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_adm_channel(
        self,
        *,
        ADMChannelRequest: dict[str, Any],
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_apns_channel(
        self,
        *,
        APNSChannelRequest: dict[str, Any],
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_apns_sandbox_channel(
        self,
        *,
        APNSSandboxChannelRequest: dict[str, Any],
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_apns_voip_channel(
        self,
        *,
        APNSVoipChannelRequest: dict[str, Any],
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_apns_voip_sandbox_channel(
        self,
        *,
        APNSVoipSandboxChannelRequest: dict[str, Any],
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_application_settings(
        self,
        *,
        ApplicationId: str,
        WriteApplicationSettingsRequest: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_baidu_channel(
        self,
        *,
        ApplicationId: str,
        BaiduChannelRequest: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_campaign(
        self,
        *,
        ApplicationId: str,
        CampaignId: str,
        WriteCampaignRequest: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_email_channel(
        self,
        *,
        ApplicationId: str,
        EmailChannelRequest: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_email_template(
        self,
        *,
        EmailTemplateRequest: dict[str, Any],
        TemplateName: str,
        CreateNewVersion: bool | None = None,
        Version: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_endpoint(
        self,
        *,
        ApplicationId: str,
        EndpointId: str,
        EndpointRequest: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_endpoints_batch(
        self,
        *,
        ApplicationId: str,
        EndpointBatchRequest: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_gcm_channel(
        self,
        *,
        ApplicationId: str,
        GCMChannelRequest: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_in_app_template(
        self,
        *,
        InAppTemplateRequest: dict[str, Any],
        TemplateName: str,
        CreateNewVersion: bool | None = None,
        Version: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_journey(
        self,
        *,
        ApplicationId: str,
        JourneyId: str,
        WriteJourneyRequest: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_journey_state(
        self,
        *,
        ApplicationId: str,
        JourneyId: str,
        JourneyStateRequest: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_push_template(
        self,
        *,
        PushNotificationTemplateRequest: dict[str, Any],
        TemplateName: str,
        CreateNewVersion: bool | None = None,
        Version: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_recommender_configuration(
        self,
        *,
        RecommenderId: str,
        UpdateRecommenderConfiguration: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_segment(
        self,
        *,
        ApplicationId: str,
        SegmentId: str,
        WriteSegmentRequest: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_sms_channel(
        self,
        *,
        ApplicationId: str,
        SMSChannelRequest: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_sms_template(
        self,
        *,
        SMSTemplateRequest: dict[str, Any],
        TemplateName: str,
        CreateNewVersion: bool | None = None,
        Version: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_template_active_version(
        self,
        *,
        TemplateActiveVersionRequest: dict[str, Any],
        TemplateName: str,
        TemplateType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_voice_channel(
        self,
        *,
        ApplicationId: str,
        VoiceChannelRequest: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_voice_template(
        self,
        *,
        TemplateName: str,
        VoiceTemplateRequest: dict[str, Any],
        CreateNewVersion: bool | None = None,
        Version: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def verify_otp_message(
        self,
        *,
        ApplicationId: str,
        VerifyOTPMessageRequestParameters: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
