from werkflow_aws.models.pinpoint import (
    PinpointCreateAppRequest,
    PinpointCreateAppResponse,
    PinpointCreateCampaignRequest,
    PinpointCreateCampaignResponse,
    PinpointCreateEmailTemplateRequest,
    PinpointCreateEmailTemplateResponse,
    PinpointCreateExportJobRequest,
    PinpointCreateExportJobResponse,
    PinpointCreateImportJobRequest,
    PinpointCreateImportJobResponse,
    PinpointCreateInAppTemplateRequest,
    PinpointCreateInAppTemplateResponse,
    PinpointCreateJourneyRequest,
    PinpointCreateJourneyResponse,
    PinpointCreatePushTemplateRequest,
    PinpointCreatePushTemplateResponse,
    PinpointCreateRecommenderConfigurationRequest,
    PinpointCreateRecommenderConfigurationResponse,
    PinpointCreateSegmentRequest,
    PinpointCreateSegmentResponse,
    PinpointCreateSmsTemplateRequest,
    PinpointCreateSmsTemplateResponse,
    PinpointCreateVoiceTemplateRequest,
    PinpointCreateVoiceTemplateResponse,
    PinpointDeleteAdmChannelRequest,
    PinpointDeleteAdmChannelResponse,
    PinpointDeleteApnsChannelRequest,
    PinpointDeleteApnsChannelResponse,
    PinpointDeleteApnsSandboxChannelRequest,
    PinpointDeleteApnsSandboxChannelResponse,
    PinpointDeleteApnsVoipChannelRequest,
    PinpointDeleteApnsVoipChannelResponse,
    PinpointDeleteApnsVoipSandboxChannelRequest,
    PinpointDeleteApnsVoipSandboxChannelResponse,
    PinpointDeleteAppRequest,
    PinpointDeleteAppResponse,
    PinpointDeleteBaiduChannelRequest,
    PinpointDeleteBaiduChannelResponse,
    PinpointDeleteCampaignRequest,
    PinpointDeleteCampaignResponse,
    PinpointDeleteEmailChannelRequest,
    PinpointDeleteEmailChannelResponse,
    PinpointDeleteEmailTemplateRequest,
    PinpointDeleteEmailTemplateResponse,
    PinpointDeleteEndpointRequest,
    PinpointDeleteEndpointResponse,
    PinpointDeleteEventStreamRequest,
    PinpointDeleteEventStreamResponse,
    PinpointDeleteGcmChannelRequest,
    PinpointDeleteGcmChannelResponse,
    PinpointDeleteInAppTemplateRequest,
    PinpointDeleteInAppTemplateResponse,
    PinpointDeleteJourneyRequest,
    PinpointDeleteJourneyResponse,
    PinpointDeletePushTemplateRequest,
    PinpointDeletePushTemplateResponse,
    PinpointDeleteRecommenderConfigurationRequest,
    PinpointDeleteRecommenderConfigurationResponse,
    PinpointDeleteSegmentRequest,
    PinpointDeleteSegmentResponse,
    PinpointDeleteSmsChannelRequest,
    PinpointDeleteSmsChannelResponse,
    PinpointDeleteSmsTemplateRequest,
    PinpointDeleteSmsTemplateResponse,
    PinpointDeleteUserEndpointsRequest,
    PinpointDeleteUserEndpointsResponse,
    PinpointDeleteVoiceChannelRequest,
    PinpointDeleteVoiceChannelResponse,
    PinpointDeleteVoiceTemplateRequest,
    PinpointDeleteVoiceTemplateResponse,
    PinpointGetAdmChannelRequest,
    PinpointGetAdmChannelResponse,
    PinpointGetApnsChannelRequest,
    PinpointGetApnsChannelResponse,
    PinpointGetApnsSandboxChannelRequest,
    PinpointGetApnsSandboxChannelResponse,
    PinpointGetApnsVoipChannelRequest,
    PinpointGetApnsVoipChannelResponse,
    PinpointGetApnsVoipSandboxChannelRequest,
    PinpointGetApnsVoipSandboxChannelResponse,
    PinpointGetAppRequest,
    PinpointGetAppResponse,
    PinpointGetApplicationDateRangeKpiRequest,
    PinpointGetApplicationDateRangeKpiResponse,
    PinpointGetApplicationSettingsRequest,
    PinpointGetApplicationSettingsResponse,
    PinpointGetAppsRequest,
    PinpointGetAppsResponse,
    PinpointGetBaiduChannelRequest,
    PinpointGetBaiduChannelResponse,
    PinpointGetCampaignActivitiesRequest,
    PinpointGetCampaignActivitiesResponse,
    PinpointGetCampaignDateRangeKpiRequest,
    PinpointGetCampaignDateRangeKpiResponse,
    PinpointGetCampaignRequest,
    PinpointGetCampaignResponse,
    PinpointGetCampaignVersionRequest,
    PinpointGetCampaignVersionResponse,
    PinpointGetCampaignVersionsRequest,
    PinpointGetCampaignVersionsResponse,
    PinpointGetCampaignsRequest,
    PinpointGetCampaignsResponse,
    PinpointGetChannelsRequest,
    PinpointGetChannelsResponse,
    PinpointGetEmailChannelRequest,
    PinpointGetEmailChannelResponse,
    PinpointGetEmailTemplateRequest,
    PinpointGetEmailTemplateResponse,
    PinpointGetEndpointRequest,
    PinpointGetEndpointResponse,
    PinpointGetEventStreamRequest,
    PinpointGetEventStreamResponse,
    PinpointGetExportJobRequest,
    PinpointGetExportJobResponse,
    PinpointGetExportJobsRequest,
    PinpointGetExportJobsResponse,
    PinpointGetGcmChannelRequest,
    PinpointGetGcmChannelResponse,
    PinpointGetImportJobRequest,
    PinpointGetImportJobResponse,
    PinpointGetImportJobsRequest,
    PinpointGetImportJobsResponse,
    PinpointGetInAppMessagesRequest,
    PinpointGetInAppMessagesResponse,
    PinpointGetInAppTemplateRequest,
    PinpointGetInAppTemplateResponse,
    PinpointGetJourneyDateRangeKpiRequest,
    PinpointGetJourneyDateRangeKpiResponse,
    PinpointGetJourneyExecutionActivityMetricsRequest,
    PinpointGetJourneyExecutionActivityMetricsResponse,
    PinpointGetJourneyExecutionMetricsRequest,
    PinpointGetJourneyExecutionMetricsResponse,
    PinpointGetJourneyRequest,
    PinpointGetJourneyResponse,
    PinpointGetJourneyRunExecutionActivityMetricsRequest,
    PinpointGetJourneyRunExecutionActivityMetricsResponse,
    PinpointGetJourneyRunExecutionMetricsRequest,
    PinpointGetJourneyRunExecutionMetricsResponse,
    PinpointGetJourneyRunsRequest,
    PinpointGetJourneyRunsResponse,
    PinpointGetPushTemplateRequest,
    PinpointGetPushTemplateResponse,
    PinpointGetRecommenderConfigurationRequest,
    PinpointGetRecommenderConfigurationResponse,
    PinpointGetRecommenderConfigurationsRequest,
    PinpointGetRecommenderConfigurationsResponse,
    PinpointGetSegmentExportJobsRequest,
    PinpointGetSegmentExportJobsResponse,
    PinpointGetSegmentImportJobsRequest,
    PinpointGetSegmentImportJobsResponse,
    PinpointGetSegmentRequest,
    PinpointGetSegmentResponse,
    PinpointGetSegmentVersionRequest,
    PinpointGetSegmentVersionResponse,
    PinpointGetSegmentVersionsRequest,
    PinpointGetSegmentVersionsResponse,
    PinpointGetSegmentsRequest,
    PinpointGetSegmentsResponse,
    PinpointGetSmsChannelRequest,
    PinpointGetSmsChannelResponse,
    PinpointGetSmsTemplateRequest,
    PinpointGetSmsTemplateResponse,
    PinpointGetUserEndpointsRequest,
    PinpointGetUserEndpointsResponse,
    PinpointGetVoiceChannelRequest,
    PinpointGetVoiceChannelResponse,
    PinpointGetVoiceTemplateRequest,
    PinpointGetVoiceTemplateResponse,
    PinpointListJourneysRequest,
    PinpointListJourneysResponse,
    PinpointListTagsForResourceRequest,
    PinpointListTagsForResourceResponse,
    PinpointListTemplateVersionsRequest,
    PinpointListTemplateVersionsResponse,
    PinpointListTemplatesRequest,
    PinpointListTemplatesResponse,
    PinpointPhoneNumberValidateRequest,
    PinpointPhoneNumberValidateResponse,
    PinpointPutEventStreamRequest,
    PinpointPutEventStreamResponse,
    PinpointPutEventsRequest,
    PinpointPutEventsResponse,
    PinpointRemoveAttributesRequest,
    PinpointRemoveAttributesResponse,
    PinpointSendMessagesRequest,
    PinpointSendMessagesResponse,
    PinpointSendOTPMessageRequest,
    PinpointSendOTPMessageResponse,
    PinpointSendUsersMessagesRequest,
    PinpointSendUsersMessagesResponse,
    PinpointTagResourceRequest,
    PinpointTagResourceResponse,
    PinpointUntagResourceRequest,
    PinpointUntagResourceResponse,
    PinpointUpdateAdmChannelRequest,
    PinpointUpdateAdmChannelResponse,
    PinpointUpdateApnsChannelRequest,
    PinpointUpdateApnsChannelResponse,
    PinpointUpdateApnsSandboxChannelRequest,
    PinpointUpdateApnsSandboxChannelResponse,
    PinpointUpdateApnsVoipChannelRequest,
    PinpointUpdateApnsVoipChannelResponse,
    PinpointUpdateApnsVoipSandboxChannelRequest,
    PinpointUpdateApnsVoipSandboxChannelResponse,
    PinpointUpdateApplicationSettingsRequest,
    PinpointUpdateApplicationSettingsResponse,
    PinpointUpdateBaiduChannelRequest,
    PinpointUpdateBaiduChannelResponse,
    PinpointUpdateCampaignRequest,
    PinpointUpdateCampaignResponse,
    PinpointUpdateEmailChannelRequest,
    PinpointUpdateEmailChannelResponse,
    PinpointUpdateEmailTemplateRequest,
    PinpointUpdateEmailTemplateResponse,
    PinpointUpdateEndpointRequest,
    PinpointUpdateEndpointResponse,
    PinpointUpdateEndpointsBatchRequest,
    PinpointUpdateEndpointsBatchResponse,
    PinpointUpdateGcmChannelRequest,
    PinpointUpdateGcmChannelResponse,
    PinpointUpdateInAppTemplateRequest,
    PinpointUpdateInAppTemplateResponse,
    PinpointUpdateJourneyRequest,
    PinpointUpdateJourneyResponse,
    PinpointUpdateJourneyStateRequest,
    PinpointUpdateJourneyStateResponse,
    PinpointUpdatePushTemplateRequest,
    PinpointUpdatePushTemplateResponse,
    PinpointUpdateRecommenderConfigurationRequest,
    PinpointUpdateRecommenderConfigurationResponse,
    PinpointUpdateSegmentRequest,
    PinpointUpdateSegmentResponse,
    PinpointUpdateSmsChannelRequest,
    PinpointUpdateSmsChannelResponse,
    PinpointUpdateSmsTemplateRequest,
    PinpointUpdateSmsTemplateResponse,
    PinpointUpdateTemplateActiveVersionRequest,
    PinpointUpdateTemplateActiveVersionResponse,
    PinpointUpdateVoiceChannelRequest,
    PinpointUpdateVoiceChannelResponse,
    PinpointUpdateVoiceTemplateRequest,
    PinpointUpdateVoiceTemplateResponse,
    PinpointVerifyOTPMessageRequest,
    PinpointVerifyOTPMessageResponse,
)
from werkflow_aws.types.pinpoint_client import PinpointClient
from .base import AWSBaseService


class AWSPinpoint(AWSBaseService[PinpointClient]):
    service_name = 'pinpoint'
    boto3_service_name = 'pinpoint'

    def __init__(self) -> None:
        super().__init__(service_name='pinpoint', boto3_service_name='pinpoint')

    async def create_app(
        self,
        request: PinpointCreateAppRequest,
    ) -> PinpointCreateAppResponse:
        client = self._require_client()
        return await self._execute(client.create_app, request, PinpointCreateAppResponse)

    async def create_campaign(
        self,
        request: PinpointCreateCampaignRequest,
    ) -> PinpointCreateCampaignResponse:
        client = self._require_client()
        return await self._execute(client.create_campaign, request, PinpointCreateCampaignResponse)

    async def create_email_template(
        self,
        request: PinpointCreateEmailTemplateRequest,
    ) -> PinpointCreateEmailTemplateResponse:
        client = self._require_client()
        return await self._execute(client.create_email_template, request, PinpointCreateEmailTemplateResponse)

    async def create_export_job(
        self,
        request: PinpointCreateExportJobRequest,
    ) -> PinpointCreateExportJobResponse:
        client = self._require_client()
        return await self._execute(client.create_export_job, request, PinpointCreateExportJobResponse)

    async def create_import_job(
        self,
        request: PinpointCreateImportJobRequest,
    ) -> PinpointCreateImportJobResponse:
        client = self._require_client()
        return await self._execute(client.create_import_job, request, PinpointCreateImportJobResponse)

    async def create_in_app_template(
        self,
        request: PinpointCreateInAppTemplateRequest,
    ) -> PinpointCreateInAppTemplateResponse:
        client = self._require_client()
        return await self._execute(client.create_in_app_template, request, PinpointCreateInAppTemplateResponse)

    async def create_journey(
        self,
        request: PinpointCreateJourneyRequest,
    ) -> PinpointCreateJourneyResponse:
        client = self._require_client()
        return await self._execute(client.create_journey, request, PinpointCreateJourneyResponse)

    async def create_push_template(
        self,
        request: PinpointCreatePushTemplateRequest,
    ) -> PinpointCreatePushTemplateResponse:
        client = self._require_client()
        return await self._execute(client.create_push_template, request, PinpointCreatePushTemplateResponse)

    async def create_recommender_configuration(
        self,
        request: PinpointCreateRecommenderConfigurationRequest,
    ) -> PinpointCreateRecommenderConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.create_recommender_configuration, request, PinpointCreateRecommenderConfigurationResponse)

    async def create_segment(
        self,
        request: PinpointCreateSegmentRequest,
    ) -> PinpointCreateSegmentResponse:
        client = self._require_client()
        return await self._execute(client.create_segment, request, PinpointCreateSegmentResponse)

    async def create_sms_template(
        self,
        request: PinpointCreateSmsTemplateRequest,
    ) -> PinpointCreateSmsTemplateResponse:
        client = self._require_client()
        return await self._execute(client.create_sms_template, request, PinpointCreateSmsTemplateResponse)

    async def create_voice_template(
        self,
        request: PinpointCreateVoiceTemplateRequest,
    ) -> PinpointCreateVoiceTemplateResponse:
        client = self._require_client()
        return await self._execute(client.create_voice_template, request, PinpointCreateVoiceTemplateResponse)

    async def delete_adm_channel(
        self,
        request: PinpointDeleteAdmChannelRequest,
    ) -> PinpointDeleteAdmChannelResponse:
        client = self._require_client()
        return await self._execute(client.delete_adm_channel, request, PinpointDeleteAdmChannelResponse)

    async def delete_apns_channel(
        self,
        request: PinpointDeleteApnsChannelRequest,
    ) -> PinpointDeleteApnsChannelResponse:
        client = self._require_client()
        return await self._execute(client.delete_apns_channel, request, PinpointDeleteApnsChannelResponse)

    async def delete_apns_sandbox_channel(
        self,
        request: PinpointDeleteApnsSandboxChannelRequest,
    ) -> PinpointDeleteApnsSandboxChannelResponse:
        client = self._require_client()
        return await self._execute(client.delete_apns_sandbox_channel, request, PinpointDeleteApnsSandboxChannelResponse)

    async def delete_apns_voip_channel(
        self,
        request: PinpointDeleteApnsVoipChannelRequest,
    ) -> PinpointDeleteApnsVoipChannelResponse:
        client = self._require_client()
        return await self._execute(client.delete_apns_voip_channel, request, PinpointDeleteApnsVoipChannelResponse)

    async def delete_apns_voip_sandbox_channel(
        self,
        request: PinpointDeleteApnsVoipSandboxChannelRequest,
    ) -> PinpointDeleteApnsVoipSandboxChannelResponse:
        client = self._require_client()
        return await self._execute(client.delete_apns_voip_sandbox_channel, request, PinpointDeleteApnsVoipSandboxChannelResponse)

    async def delete_app(
        self,
        request: PinpointDeleteAppRequest,
    ) -> PinpointDeleteAppResponse:
        client = self._require_client()
        return await self._execute(client.delete_app, request, PinpointDeleteAppResponse)

    async def delete_baidu_channel(
        self,
        request: PinpointDeleteBaiduChannelRequest,
    ) -> PinpointDeleteBaiduChannelResponse:
        client = self._require_client()
        return await self._execute(client.delete_baidu_channel, request, PinpointDeleteBaiduChannelResponse)

    async def delete_campaign(
        self,
        request: PinpointDeleteCampaignRequest,
    ) -> PinpointDeleteCampaignResponse:
        client = self._require_client()
        return await self._execute(client.delete_campaign, request, PinpointDeleteCampaignResponse)

    async def delete_email_channel(
        self,
        request: PinpointDeleteEmailChannelRequest,
    ) -> PinpointDeleteEmailChannelResponse:
        client = self._require_client()
        return await self._execute(client.delete_email_channel, request, PinpointDeleteEmailChannelResponse)

    async def delete_email_template(
        self,
        request: PinpointDeleteEmailTemplateRequest,
    ) -> PinpointDeleteEmailTemplateResponse:
        client = self._require_client()
        return await self._execute(client.delete_email_template, request, PinpointDeleteEmailTemplateResponse)

    async def delete_endpoint(
        self,
        request: PinpointDeleteEndpointRequest,
    ) -> PinpointDeleteEndpointResponse:
        client = self._require_client()
        return await self._execute(client.delete_endpoint, request, PinpointDeleteEndpointResponse)

    async def delete_event_stream(
        self,
        request: PinpointDeleteEventStreamRequest,
    ) -> PinpointDeleteEventStreamResponse:
        client = self._require_client()
        return await self._execute(client.delete_event_stream, request, PinpointDeleteEventStreamResponse)

    async def delete_gcm_channel(
        self,
        request: PinpointDeleteGcmChannelRequest,
    ) -> PinpointDeleteGcmChannelResponse:
        client = self._require_client()
        return await self._execute(client.delete_gcm_channel, request, PinpointDeleteGcmChannelResponse)

    async def delete_in_app_template(
        self,
        request: PinpointDeleteInAppTemplateRequest,
    ) -> PinpointDeleteInAppTemplateResponse:
        client = self._require_client()
        return await self._execute(client.delete_in_app_template, request, PinpointDeleteInAppTemplateResponse)

    async def delete_journey(
        self,
        request: PinpointDeleteJourneyRequest,
    ) -> PinpointDeleteJourneyResponse:
        client = self._require_client()
        return await self._execute(client.delete_journey, request, PinpointDeleteJourneyResponse)

    async def delete_push_template(
        self,
        request: PinpointDeletePushTemplateRequest,
    ) -> PinpointDeletePushTemplateResponse:
        client = self._require_client()
        return await self._execute(client.delete_push_template, request, PinpointDeletePushTemplateResponse)

    async def delete_recommender_configuration(
        self,
        request: PinpointDeleteRecommenderConfigurationRequest,
    ) -> PinpointDeleteRecommenderConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_recommender_configuration, request, PinpointDeleteRecommenderConfigurationResponse)

    async def delete_segment(
        self,
        request: PinpointDeleteSegmentRequest,
    ) -> PinpointDeleteSegmentResponse:
        client = self._require_client()
        return await self._execute(client.delete_segment, request, PinpointDeleteSegmentResponse)

    async def delete_sms_channel(
        self,
        request: PinpointDeleteSmsChannelRequest,
    ) -> PinpointDeleteSmsChannelResponse:
        client = self._require_client()
        return await self._execute(client.delete_sms_channel, request, PinpointDeleteSmsChannelResponse)

    async def delete_sms_template(
        self,
        request: PinpointDeleteSmsTemplateRequest,
    ) -> PinpointDeleteSmsTemplateResponse:
        client = self._require_client()
        return await self._execute(client.delete_sms_template, request, PinpointDeleteSmsTemplateResponse)

    async def delete_user_endpoints(
        self,
        request: PinpointDeleteUserEndpointsRequest,
    ) -> PinpointDeleteUserEndpointsResponse:
        client = self._require_client()
        return await self._execute(client.delete_user_endpoints, request, PinpointDeleteUserEndpointsResponse)

    async def delete_voice_channel(
        self,
        request: PinpointDeleteVoiceChannelRequest,
    ) -> PinpointDeleteVoiceChannelResponse:
        client = self._require_client()
        return await self._execute(client.delete_voice_channel, request, PinpointDeleteVoiceChannelResponse)

    async def delete_voice_template(
        self,
        request: PinpointDeleteVoiceTemplateRequest,
    ) -> PinpointDeleteVoiceTemplateResponse:
        client = self._require_client()
        return await self._execute(client.delete_voice_template, request, PinpointDeleteVoiceTemplateResponse)

    async def get_adm_channel(
        self,
        request: PinpointGetAdmChannelRequest,
    ) -> PinpointGetAdmChannelResponse:
        client = self._require_client()
        return await self._execute(client.get_adm_channel, request, PinpointGetAdmChannelResponse)

    async def get_apns_channel(
        self,
        request: PinpointGetApnsChannelRequest,
    ) -> PinpointGetApnsChannelResponse:
        client = self._require_client()
        return await self._execute(client.get_apns_channel, request, PinpointGetApnsChannelResponse)

    async def get_apns_sandbox_channel(
        self,
        request: PinpointGetApnsSandboxChannelRequest,
    ) -> PinpointGetApnsSandboxChannelResponse:
        client = self._require_client()
        return await self._execute(client.get_apns_sandbox_channel, request, PinpointGetApnsSandboxChannelResponse)

    async def get_apns_voip_channel(
        self,
        request: PinpointGetApnsVoipChannelRequest,
    ) -> PinpointGetApnsVoipChannelResponse:
        client = self._require_client()
        return await self._execute(client.get_apns_voip_channel, request, PinpointGetApnsVoipChannelResponse)

    async def get_apns_voip_sandbox_channel(
        self,
        request: PinpointGetApnsVoipSandboxChannelRequest,
    ) -> PinpointGetApnsVoipSandboxChannelResponse:
        client = self._require_client()
        return await self._execute(client.get_apns_voip_sandbox_channel, request, PinpointGetApnsVoipSandboxChannelResponse)

    async def get_app(
        self,
        request: PinpointGetAppRequest,
    ) -> PinpointGetAppResponse:
        client = self._require_client()
        return await self._execute(client.get_app, request, PinpointGetAppResponse)

    async def get_application_date_range_kpi(
        self,
        request: PinpointGetApplicationDateRangeKpiRequest,
    ) -> PinpointGetApplicationDateRangeKpiResponse:
        client = self._require_client()
        return await self._execute(client.get_application_date_range_kpi, request, PinpointGetApplicationDateRangeKpiResponse)

    async def get_application_settings(
        self,
        request: PinpointGetApplicationSettingsRequest,
    ) -> PinpointGetApplicationSettingsResponse:
        client = self._require_client()
        return await self._execute(client.get_application_settings, request, PinpointGetApplicationSettingsResponse)

    async def get_apps(
        self,
        request: PinpointGetAppsRequest | None = None,
    ) -> PinpointGetAppsResponse:
        client = self._require_client()
        return await self._execute(client.get_apps, request, PinpointGetAppsResponse)

    async def get_baidu_channel(
        self,
        request: PinpointGetBaiduChannelRequest,
    ) -> PinpointGetBaiduChannelResponse:
        client = self._require_client()
        return await self._execute(client.get_baidu_channel, request, PinpointGetBaiduChannelResponse)

    async def get_campaign(
        self,
        request: PinpointGetCampaignRequest,
    ) -> PinpointGetCampaignResponse:
        client = self._require_client()
        return await self._execute(client.get_campaign, request, PinpointGetCampaignResponse)

    async def get_campaign_activities(
        self,
        request: PinpointGetCampaignActivitiesRequest,
    ) -> PinpointGetCampaignActivitiesResponse:
        client = self._require_client()
        return await self._execute(client.get_campaign_activities, request, PinpointGetCampaignActivitiesResponse)

    async def get_campaign_date_range_kpi(
        self,
        request: PinpointGetCampaignDateRangeKpiRequest,
    ) -> PinpointGetCampaignDateRangeKpiResponse:
        client = self._require_client()
        return await self._execute(client.get_campaign_date_range_kpi, request, PinpointGetCampaignDateRangeKpiResponse)

    async def get_campaign_version(
        self,
        request: PinpointGetCampaignVersionRequest,
    ) -> PinpointGetCampaignVersionResponse:
        client = self._require_client()
        return await self._execute(client.get_campaign_version, request, PinpointGetCampaignVersionResponse)

    async def get_campaign_versions(
        self,
        request: PinpointGetCampaignVersionsRequest,
    ) -> PinpointGetCampaignVersionsResponse:
        client = self._require_client()
        return await self._execute(client.get_campaign_versions, request, PinpointGetCampaignVersionsResponse)

    async def get_campaigns(
        self,
        request: PinpointGetCampaignsRequest,
    ) -> PinpointGetCampaignsResponse:
        client = self._require_client()
        return await self._execute(client.get_campaigns, request, PinpointGetCampaignsResponse)

    async def get_channels(
        self,
        request: PinpointGetChannelsRequest,
    ) -> PinpointGetChannelsResponse:
        client = self._require_client()
        return await self._execute(client.get_channels, request, PinpointGetChannelsResponse)

    async def get_email_channel(
        self,
        request: PinpointGetEmailChannelRequest,
    ) -> PinpointGetEmailChannelResponse:
        client = self._require_client()
        return await self._execute(client.get_email_channel, request, PinpointGetEmailChannelResponse)

    async def get_email_template(
        self,
        request: PinpointGetEmailTemplateRequest,
    ) -> PinpointGetEmailTemplateResponse:
        client = self._require_client()
        return await self._execute(client.get_email_template, request, PinpointGetEmailTemplateResponse)

    async def get_endpoint(
        self,
        request: PinpointGetEndpointRequest,
    ) -> PinpointGetEndpointResponse:
        client = self._require_client()
        return await self._execute(client.get_endpoint, request, PinpointGetEndpointResponse)

    async def get_event_stream(
        self,
        request: PinpointGetEventStreamRequest,
    ) -> PinpointGetEventStreamResponse:
        client = self._require_client()
        return await self._execute(client.get_event_stream, request, PinpointGetEventStreamResponse)

    async def get_export_job(
        self,
        request: PinpointGetExportJobRequest,
    ) -> PinpointGetExportJobResponse:
        client = self._require_client()
        return await self._execute(client.get_export_job, request, PinpointGetExportJobResponse)

    async def get_export_jobs(
        self,
        request: PinpointGetExportJobsRequest,
    ) -> PinpointGetExportJobsResponse:
        client = self._require_client()
        return await self._execute(client.get_export_jobs, request, PinpointGetExportJobsResponse)

    async def get_gcm_channel(
        self,
        request: PinpointGetGcmChannelRequest,
    ) -> PinpointGetGcmChannelResponse:
        client = self._require_client()
        return await self._execute(client.get_gcm_channel, request, PinpointGetGcmChannelResponse)

    async def get_import_job(
        self,
        request: PinpointGetImportJobRequest,
    ) -> PinpointGetImportJobResponse:
        client = self._require_client()
        return await self._execute(client.get_import_job, request, PinpointGetImportJobResponse)

    async def get_import_jobs(
        self,
        request: PinpointGetImportJobsRequest,
    ) -> PinpointGetImportJobsResponse:
        client = self._require_client()
        return await self._execute(client.get_import_jobs, request, PinpointGetImportJobsResponse)

    async def get_in_app_messages(
        self,
        request: PinpointGetInAppMessagesRequest,
    ) -> PinpointGetInAppMessagesResponse:
        client = self._require_client()
        return await self._execute(client.get_in_app_messages, request, PinpointGetInAppMessagesResponse)

    async def get_in_app_template(
        self,
        request: PinpointGetInAppTemplateRequest,
    ) -> PinpointGetInAppTemplateResponse:
        client = self._require_client()
        return await self._execute(client.get_in_app_template, request, PinpointGetInAppTemplateResponse)

    async def get_journey(
        self,
        request: PinpointGetJourneyRequest,
    ) -> PinpointGetJourneyResponse:
        client = self._require_client()
        return await self._execute(client.get_journey, request, PinpointGetJourneyResponse)

    async def get_journey_date_range_kpi(
        self,
        request: PinpointGetJourneyDateRangeKpiRequest,
    ) -> PinpointGetJourneyDateRangeKpiResponse:
        client = self._require_client()
        return await self._execute(client.get_journey_date_range_kpi, request, PinpointGetJourneyDateRangeKpiResponse)

    async def get_journey_execution_activity_metrics(
        self,
        request: PinpointGetJourneyExecutionActivityMetricsRequest,
    ) -> PinpointGetJourneyExecutionActivityMetricsResponse:
        client = self._require_client()
        return await self._execute(client.get_journey_execution_activity_metrics, request, PinpointGetJourneyExecutionActivityMetricsResponse)

    async def get_journey_execution_metrics(
        self,
        request: PinpointGetJourneyExecutionMetricsRequest,
    ) -> PinpointGetJourneyExecutionMetricsResponse:
        client = self._require_client()
        return await self._execute(client.get_journey_execution_metrics, request, PinpointGetJourneyExecutionMetricsResponse)

    async def get_journey_run_execution_activity_metrics(
        self,
        request: PinpointGetJourneyRunExecutionActivityMetricsRequest,
    ) -> PinpointGetJourneyRunExecutionActivityMetricsResponse:
        client = self._require_client()
        return await self._execute(client.get_journey_run_execution_activity_metrics, request, PinpointGetJourneyRunExecutionActivityMetricsResponse)

    async def get_journey_run_execution_metrics(
        self,
        request: PinpointGetJourneyRunExecutionMetricsRequest,
    ) -> PinpointGetJourneyRunExecutionMetricsResponse:
        client = self._require_client()
        return await self._execute(client.get_journey_run_execution_metrics, request, PinpointGetJourneyRunExecutionMetricsResponse)

    async def get_journey_runs(
        self,
        request: PinpointGetJourneyRunsRequest,
    ) -> PinpointGetJourneyRunsResponse:
        client = self._require_client()
        return await self._execute(client.get_journey_runs, request, PinpointGetJourneyRunsResponse)

    async def get_push_template(
        self,
        request: PinpointGetPushTemplateRequest,
    ) -> PinpointGetPushTemplateResponse:
        client = self._require_client()
        return await self._execute(client.get_push_template, request, PinpointGetPushTemplateResponse)

    async def get_recommender_configuration(
        self,
        request: PinpointGetRecommenderConfigurationRequest,
    ) -> PinpointGetRecommenderConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_recommender_configuration, request, PinpointGetRecommenderConfigurationResponse)

    async def get_recommender_configurations(
        self,
        request: PinpointGetRecommenderConfigurationsRequest | None = None,
    ) -> PinpointGetRecommenderConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.get_recommender_configurations, request, PinpointGetRecommenderConfigurationsResponse)

    async def get_segment(
        self,
        request: PinpointGetSegmentRequest,
    ) -> PinpointGetSegmentResponse:
        client = self._require_client()
        return await self._execute(client.get_segment, request, PinpointGetSegmentResponse)

    async def get_segment_export_jobs(
        self,
        request: PinpointGetSegmentExportJobsRequest,
    ) -> PinpointGetSegmentExportJobsResponse:
        client = self._require_client()
        return await self._execute(client.get_segment_export_jobs, request, PinpointGetSegmentExportJobsResponse)

    async def get_segment_import_jobs(
        self,
        request: PinpointGetSegmentImportJobsRequest,
    ) -> PinpointGetSegmentImportJobsResponse:
        client = self._require_client()
        return await self._execute(client.get_segment_import_jobs, request, PinpointGetSegmentImportJobsResponse)

    async def get_segment_version(
        self,
        request: PinpointGetSegmentVersionRequest,
    ) -> PinpointGetSegmentVersionResponse:
        client = self._require_client()
        return await self._execute(client.get_segment_version, request, PinpointGetSegmentVersionResponse)

    async def get_segment_versions(
        self,
        request: PinpointGetSegmentVersionsRequest,
    ) -> PinpointGetSegmentVersionsResponse:
        client = self._require_client()
        return await self._execute(client.get_segment_versions, request, PinpointGetSegmentVersionsResponse)

    async def get_segments(
        self,
        request: PinpointGetSegmentsRequest,
    ) -> PinpointGetSegmentsResponse:
        client = self._require_client()
        return await self._execute(client.get_segments, request, PinpointGetSegmentsResponse)

    async def get_sms_channel(
        self,
        request: PinpointGetSmsChannelRequest,
    ) -> PinpointGetSmsChannelResponse:
        client = self._require_client()
        return await self._execute(client.get_sms_channel, request, PinpointGetSmsChannelResponse)

    async def get_sms_template(
        self,
        request: PinpointGetSmsTemplateRequest,
    ) -> PinpointGetSmsTemplateResponse:
        client = self._require_client()
        return await self._execute(client.get_sms_template, request, PinpointGetSmsTemplateResponse)

    async def get_user_endpoints(
        self,
        request: PinpointGetUserEndpointsRequest,
    ) -> PinpointGetUserEndpointsResponse:
        client = self._require_client()
        return await self._execute(client.get_user_endpoints, request, PinpointGetUserEndpointsResponse)

    async def get_voice_channel(
        self,
        request: PinpointGetVoiceChannelRequest,
    ) -> PinpointGetVoiceChannelResponse:
        client = self._require_client()
        return await self._execute(client.get_voice_channel, request, PinpointGetVoiceChannelResponse)

    async def get_voice_template(
        self,
        request: PinpointGetVoiceTemplateRequest,
    ) -> PinpointGetVoiceTemplateResponse:
        client = self._require_client()
        return await self._execute(client.get_voice_template, request, PinpointGetVoiceTemplateResponse)

    async def list_journeys(
        self,
        request: PinpointListJourneysRequest,
    ) -> PinpointListJourneysResponse:
        client = self._require_client()
        return await self._execute(client.list_journeys, request, PinpointListJourneysResponse)

    async def list_tags_for_resource(
        self,
        request: PinpointListTagsForResourceRequest,
    ) -> PinpointListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, PinpointListTagsForResourceResponse)

    async def list_template_versions(
        self,
        request: PinpointListTemplateVersionsRequest,
    ) -> PinpointListTemplateVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_template_versions, request, PinpointListTemplateVersionsResponse)

    async def list_templates(
        self,
        request: PinpointListTemplatesRequest | None = None,
    ) -> PinpointListTemplatesResponse:
        client = self._require_client()
        return await self._execute(client.list_templates, request, PinpointListTemplatesResponse)

    async def phone_number_validate(
        self,
        request: PinpointPhoneNumberValidateRequest,
    ) -> PinpointPhoneNumberValidateResponse:
        client = self._require_client()
        return await self._execute(client.phone_number_validate, request, PinpointPhoneNumberValidateResponse)

    async def put_event_stream(
        self,
        request: PinpointPutEventStreamRequest,
    ) -> PinpointPutEventStreamResponse:
        client = self._require_client()
        return await self._execute(client.put_event_stream, request, PinpointPutEventStreamResponse)

    async def put_events(
        self,
        request: PinpointPutEventsRequest,
    ) -> PinpointPutEventsResponse:
        client = self._require_client()
        return await self._execute(client.put_events, request, PinpointPutEventsResponse)

    async def remove_attributes(
        self,
        request: PinpointRemoveAttributesRequest,
    ) -> PinpointRemoveAttributesResponse:
        client = self._require_client()
        return await self._execute(client.remove_attributes, request, PinpointRemoveAttributesResponse)

    async def send_messages(
        self,
        request: PinpointSendMessagesRequest,
    ) -> PinpointSendMessagesResponse:
        client = self._require_client()
        return await self._execute(client.send_messages, request, PinpointSendMessagesResponse)

    async def send_otp_message(
        self,
        request: PinpointSendOTPMessageRequest,
    ) -> PinpointSendOTPMessageResponse:
        client = self._require_client()
        return await self._execute(client.send_otp_message, request, PinpointSendOTPMessageResponse)

    async def send_users_messages(
        self,
        request: PinpointSendUsersMessagesRequest,
    ) -> PinpointSendUsersMessagesResponse:
        client = self._require_client()
        return await self._execute(client.send_users_messages, request, PinpointSendUsersMessagesResponse)

    async def tag_resource(
        self,
        request: PinpointTagResourceRequest,
    ) -> PinpointTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, PinpointTagResourceResponse)

    async def untag_resource(
        self,
        request: PinpointUntagResourceRequest,
    ) -> PinpointUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, PinpointUntagResourceResponse)

    async def update_adm_channel(
        self,
        request: PinpointUpdateAdmChannelRequest,
    ) -> PinpointUpdateAdmChannelResponse:
        client = self._require_client()
        return await self._execute(client.update_adm_channel, request, PinpointUpdateAdmChannelResponse)

    async def update_apns_channel(
        self,
        request: PinpointUpdateApnsChannelRequest,
    ) -> PinpointUpdateApnsChannelResponse:
        client = self._require_client()
        return await self._execute(client.update_apns_channel, request, PinpointUpdateApnsChannelResponse)

    async def update_apns_sandbox_channel(
        self,
        request: PinpointUpdateApnsSandboxChannelRequest,
    ) -> PinpointUpdateApnsSandboxChannelResponse:
        client = self._require_client()
        return await self._execute(client.update_apns_sandbox_channel, request, PinpointUpdateApnsSandboxChannelResponse)

    async def update_apns_voip_channel(
        self,
        request: PinpointUpdateApnsVoipChannelRequest,
    ) -> PinpointUpdateApnsVoipChannelResponse:
        client = self._require_client()
        return await self._execute(client.update_apns_voip_channel, request, PinpointUpdateApnsVoipChannelResponse)

    async def update_apns_voip_sandbox_channel(
        self,
        request: PinpointUpdateApnsVoipSandboxChannelRequest,
    ) -> PinpointUpdateApnsVoipSandboxChannelResponse:
        client = self._require_client()
        return await self._execute(client.update_apns_voip_sandbox_channel, request, PinpointUpdateApnsVoipSandboxChannelResponse)

    async def update_application_settings(
        self,
        request: PinpointUpdateApplicationSettingsRequest,
    ) -> PinpointUpdateApplicationSettingsResponse:
        client = self._require_client()
        return await self._execute(client.update_application_settings, request, PinpointUpdateApplicationSettingsResponse)

    async def update_baidu_channel(
        self,
        request: PinpointUpdateBaiduChannelRequest,
    ) -> PinpointUpdateBaiduChannelResponse:
        client = self._require_client()
        return await self._execute(client.update_baidu_channel, request, PinpointUpdateBaiduChannelResponse)

    async def update_campaign(
        self,
        request: PinpointUpdateCampaignRequest,
    ) -> PinpointUpdateCampaignResponse:
        client = self._require_client()
        return await self._execute(client.update_campaign, request, PinpointUpdateCampaignResponse)

    async def update_email_channel(
        self,
        request: PinpointUpdateEmailChannelRequest,
    ) -> PinpointUpdateEmailChannelResponse:
        client = self._require_client()
        return await self._execute(client.update_email_channel, request, PinpointUpdateEmailChannelResponse)

    async def update_email_template(
        self,
        request: PinpointUpdateEmailTemplateRequest,
    ) -> PinpointUpdateEmailTemplateResponse:
        client = self._require_client()
        return await self._execute(client.update_email_template, request, PinpointUpdateEmailTemplateResponse)

    async def update_endpoint(
        self,
        request: PinpointUpdateEndpointRequest,
    ) -> PinpointUpdateEndpointResponse:
        client = self._require_client()
        return await self._execute(client.update_endpoint, request, PinpointUpdateEndpointResponse)

    async def update_endpoints_batch(
        self,
        request: PinpointUpdateEndpointsBatchRequest,
    ) -> PinpointUpdateEndpointsBatchResponse:
        client = self._require_client()
        return await self._execute(client.update_endpoints_batch, request, PinpointUpdateEndpointsBatchResponse)

    async def update_gcm_channel(
        self,
        request: PinpointUpdateGcmChannelRequest,
    ) -> PinpointUpdateGcmChannelResponse:
        client = self._require_client()
        return await self._execute(client.update_gcm_channel, request, PinpointUpdateGcmChannelResponse)

    async def update_in_app_template(
        self,
        request: PinpointUpdateInAppTemplateRequest,
    ) -> PinpointUpdateInAppTemplateResponse:
        client = self._require_client()
        return await self._execute(client.update_in_app_template, request, PinpointUpdateInAppTemplateResponse)

    async def update_journey(
        self,
        request: PinpointUpdateJourneyRequest,
    ) -> PinpointUpdateJourneyResponse:
        client = self._require_client()
        return await self._execute(client.update_journey, request, PinpointUpdateJourneyResponse)

    async def update_journey_state(
        self,
        request: PinpointUpdateJourneyStateRequest,
    ) -> PinpointUpdateJourneyStateResponse:
        client = self._require_client()
        return await self._execute(client.update_journey_state, request, PinpointUpdateJourneyStateResponse)

    async def update_push_template(
        self,
        request: PinpointUpdatePushTemplateRequest,
    ) -> PinpointUpdatePushTemplateResponse:
        client = self._require_client()
        return await self._execute(client.update_push_template, request, PinpointUpdatePushTemplateResponse)

    async def update_recommender_configuration(
        self,
        request: PinpointUpdateRecommenderConfigurationRequest,
    ) -> PinpointUpdateRecommenderConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_recommender_configuration, request, PinpointUpdateRecommenderConfigurationResponse)

    async def update_segment(
        self,
        request: PinpointUpdateSegmentRequest,
    ) -> PinpointUpdateSegmentResponse:
        client = self._require_client()
        return await self._execute(client.update_segment, request, PinpointUpdateSegmentResponse)

    async def update_sms_channel(
        self,
        request: PinpointUpdateSmsChannelRequest,
    ) -> PinpointUpdateSmsChannelResponse:
        client = self._require_client()
        return await self._execute(client.update_sms_channel, request, PinpointUpdateSmsChannelResponse)

    async def update_sms_template(
        self,
        request: PinpointUpdateSmsTemplateRequest,
    ) -> PinpointUpdateSmsTemplateResponse:
        client = self._require_client()
        return await self._execute(client.update_sms_template, request, PinpointUpdateSmsTemplateResponse)

    async def update_template_active_version(
        self,
        request: PinpointUpdateTemplateActiveVersionRequest,
    ) -> PinpointUpdateTemplateActiveVersionResponse:
        client = self._require_client()
        return await self._execute(client.update_template_active_version, request, PinpointUpdateTemplateActiveVersionResponse)

    async def update_voice_channel(
        self,
        request: PinpointUpdateVoiceChannelRequest,
    ) -> PinpointUpdateVoiceChannelResponse:
        client = self._require_client()
        return await self._execute(client.update_voice_channel, request, PinpointUpdateVoiceChannelResponse)

    async def update_voice_template(
        self,
        request: PinpointUpdateVoiceTemplateRequest,
    ) -> PinpointUpdateVoiceTemplateResponse:
        client = self._require_client()
        return await self._execute(client.update_voice_template, request, PinpointUpdateVoiceTemplateResponse)

    async def verify_otp_message(
        self,
        request: PinpointVerifyOTPMessageRequest,
    ) -> PinpointVerifyOTPMessageResponse:
        client = self._require_client()
        return await self._execute(client.verify_otp_message, request, PinpointVerifyOTPMessageResponse)
