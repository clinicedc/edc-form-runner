import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from dateutil.relativedelta import relativedelta
from edc_test_settings.default_test_settings import DefaultTestSettings

app_name = "edc_form_runners"
base_dir = Path(__file__).absolute().parent.parent.parent

project_settings = DefaultTestSettings(
    calling_file=__file__,
    BASE_DIR=base_dir,
    APP_NAME=app_name,
    ETC_DIR=base_dir / app_name / "tests" / "etc",
    SILENCED_SYSTEM_CHECKS=[
        "sites.E101",
        "edc_navbar.E002",
        "edc_navbar.E003",
        "edc_sites.E001",
    ],
    EDC_NAVBAR_DEFAULT="form_runners_app",
    EDC_AUTH_CODENAMES_WARN_ONLY=True,
    EDC_AUTH_SKIP_SITE_AUTHS=True,
    EDC_AUTH_SKIP_AUTH_UPDATER=True,
    SUBJECT_VISIT_MODEL="edc_visit_tracking.subjectvisit",
    SUBJECT_VISIT_MISSED_MODEL="edc_visit_tracking.subjectvisitmissed",
    SUBJECT_SCREENING_MODEL="form_runners_app.subjectscreening",
    EDC_SITES_REGISTER_DEFAULT=False,
    ROOT_URLCONF="form_runners_app.urls",
    EDC_PROTOCOL_STUDY_OPEN_DATETIME=(
        datetime(2018, 5, 15, 0, 0, 0, tzinfo=ZoneInfo("UTC")) - relativedelta(years=1)
    ),
    EDC_PROTOCOL_STUDY_CLOSE_DATETIME=(
        datetime(2022, 5, 14, 0, 0, 0, tzinfo=ZoneInfo("UTC")) - relativedelta(years=1)
    ),
    INSTALLED_APPS=[
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django.contrib.sites",
        "django_crypto_fields.apps.AppConfig",
        "django_revision.apps.AppConfig",
        "edc_appointment.apps.AppConfig",
        "edc_auth.apps.AppConfig",
        "edc_action_item.apps.AppConfig",
        "edc_adverse_event.apps.AppConfig",
        "adverse_event_app.apps.AppConfig",
        "edc_consent.apps.AppConfig",
        "edc_data_manager.apps.AppConfig",
        "edc_dashboard.apps.AppConfig",
        "edc_device.apps.AppConfig",
        "edc_identifier.apps.AppConfig",
        "edc_facility.apps.AppConfig",
        "edc_lab.apps.AppConfig",
        "edc_metadata.apps.AppConfig",
        "edc_notification.apps.AppConfig",
        "edc_registration.apps.AppConfig",
        "edc_review_dashboard.apps.AppConfig",
        "edc_sites.apps.AppConfig",
        "edc_subject_dashboard.apps.AppConfig",
        "edc_visit_schedule.apps.AppConfig",
        "edc_visit_tracking.apps.AppConfig",
        "edc_timepoint.apps.AppConfig",
        "edc_form_runners.apps.AppConfig",
        "form_runners_app.apps.AppConfig",
        "edc_appconfig.apps.AppConfig",
    ],
    add_dashboard_middleware=True,
    use_test_urls=True,
).settings

for k, v in project_settings.items():
    setattr(sys.modules[__name__], k, v)
