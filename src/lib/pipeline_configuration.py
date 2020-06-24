import json
from abc import ABC, abstractmethod
from datetime import datetime
from urllib.parse import urlparse

import pytz
from core_data_modules.cleaners import Codes, swahili, somali
from core_data_modules.data_models import validators
from core_data_modules.traced_data.util.fold_traced_data import FoldStrategies
from dateutil.parser import isoparse

from configurations import code_imputation_functions
from configurations.code_schemes import CodeSchemes


class CodingModes(object):
    SINGLE = "SINGLE"
    MULTIPLE = "MULTIPLE"


class CodingConfiguration(object):
    def __init__(self, coding_mode, code_scheme, coded_field, fold_strategy, analysis_file_key=None, cleaner=None):
        assert coding_mode in {CodingModes.SINGLE, CodingModes.MULTIPLE}

        self.coding_mode = coding_mode
        self.code_scheme = code_scheme
        self.coded_field = coded_field
        self.analysis_file_key = analysis_file_key
        self.fold_strategy = fold_strategy
        self.cleaner = cleaner


# TODO: Rename CodingPlan to something like DatasetConfiguration?
class CodingPlan(object):
    def __init__(self, raw_field, dataset_name, coding_configurations, raw_field_fold_strategy, coda_filename=None, ws_code=None,
                 time_field=None, run_id_field=None, icr_filename=None, id_field=None, code_imputation_function=None,
                 listening_group_filename=None,):
        self.raw_field = raw_field
        self.dataset_name = dataset_name
        self.time_field = time_field
        self.run_id_field = run_id_field
        self.coda_filename = coda_filename
        self.icr_filename = icr_filename
        self.coding_configurations = coding_configurations
        self.code_imputation_function = code_imputation_function
        self.listening_group_filename = listening_group_filename
        self.ws_code = ws_code
        self.raw_field_fold_strategy = raw_field_fold_strategy

        if id_field is None:
            id_field = "{}_id".format(self.raw_field)
        self.id_field = id_field


class PipelineConfiguration(object):

    RQA_CODING_PLANS = None

    DADAAB_RQA_CODING_PLANS = [
        CodingPlan(raw_field="rqa_s01e01_raw",
                   dataset_name="dadaab_s01e01",
                   time_field="sent_on",
                   run_id_field="rqa_s01e01_run_id",
                   coda_filename="dadaab_s01e01.json",
                   icr_filename="dadaab_s01e01.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.DADAAB_S01E01,
                           coded_field="rqa_s01e01_coded",
                           analysis_file_key="rqa_s01e01_",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.DADAAB_S01E01, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.DADAAB_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("covid19 adaptation dadaab s01e01"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_s01e02_raw",
                   dataset_name="dadaab_s01e02",
                   time_field="sent_on",
                   run_id_field="rqa_s01e02_run_id",
                   coda_filename="dadaab_s01e02.json",
                   icr_filename="dadaab_s01e02.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.DADAAB_S01E02,
                           coded_field="rqa_s01e02_coded",
                           analysis_file_key="rqa_s01e02_",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.DADAAB_S01E02, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.DADAAB_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("covid19 adaptation dadaab s01e02"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_s01e03_raw",
                   dataset_name="dadaab_s01e03",
                   time_field="sent_on",
                   run_id_field="rqa_s01e03_run_id",
                   coda_filename="dadaab_s01e03.json",
                   icr_filename="dadaab_s01e03.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.DADAAB_S01E03,
                           coded_field="rqa_s01e03_coded",
                           analysis_file_key="rqa_s01e03_",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.DADAAB_S01E03, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.DADAAB_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("covid19 adaptation dadaab s01e03"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_s01e04_raw",
                   dataset_name="dadaab_s01e04",
                   time_field="sent_on",
                   run_id_field="rqa_s01e04_run_id",
                   coda_filename="dadaab_s01e04.json",
                   icr_filename="dadaab_s01e04.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.DADAAB_S01E04,
                           coded_field="rqa_s01e04_coded",
                           analysis_file_key="rqa_s01e04_",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.DADAAB_S01E04, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.DADAAB_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("covid19 adaptation dadaab s01e04"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_s01e05_raw",
                   dataset_name="dadaab_s01e05",
                   time_field="sent_on",
                   run_id_field="rqa_s01e05_run_id",
                   coda_filename="dadaab_s01e05.json",
                   icr_filename="dadaab_s01e05.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.DADAAB_S01E05,
                           coded_field="rqa_s01e05_coded",
                           analysis_file_key="rqa_s01e05_",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.DADAAB_S01E05, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.DADAAB_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("covid19 adaptation dadaab s01e05"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_s01e06_raw",
                   dataset_name="dadaab_s01e06",
                   time_field="sent_on",
                   run_id_field="rqa_s01e06_run_id",
                   coda_filename="dadaab_s01e06.json",
                   icr_filename="dadaab_s01e06.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.DADAAB_S01E06,
                           coded_field="rqa_s01e06_coded",
                           analysis_file_key="rqa_s01e06_",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.DADAAB_S01E06, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.DADAAB_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("covid19 adaptation dadaab s01e06"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_s01e07_raw",
                   dataset_name="dadaab_s01e07",
                   time_field="sent_on",
                   run_id_field="rqa_s01e07_run_id",
                   coda_filename="dadaab_s01e07.json",
                   icr_filename="dadaab_s01e07.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.DADAAB_S01E07,
                           coded_field="rqa_s01e07_coded",
                           analysis_file_key="rqa_s01e07_",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.DADAAB_S01E07, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.DADAAB_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("covid19 adaptation dadaab s01e07"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_s01e08_raw",
                   dataset_name="dadaab_s01e08",
                   time_field="sent_on",
                   run_id_field="rqa_s01e08_run_id",
                   coda_filename="dadaab_s01e08.json",
                   icr_filename="dadaab_s01e08.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.DADAAB_S01E08,
                           coded_field="rqa_s01e08_coded",
                           analysis_file_key="rqa_s01e08_",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.DADAAB_S01E08, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.DADAAB_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("covid19 adaptation dadaab s01e08"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_s01e09_raw",
                   dataset_name="dadaab_s01e09",
                   time_field="sent_on",
                   run_id_field="rqa_s01e09_run_id",
                   coda_filename="dadaab_s01e09.json",
                   icr_filename="dadaab_s01e09.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.DADAAB_S01E09,
                           coded_field="rqa_s01e09_coded",
                           analysis_file_key="rqa_s01e09_",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.DADAAB_S01E09, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.DADAAB_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("covid19 adaptation dadaab s01e09"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_s01e10_raw",
                   dataset_name="dadaab_s01e10",
                   time_field="sent_on",
                   run_id_field="rqa_s01e10_run_id",
                   coda_filename="dadaab_s01e10.json",
                   icr_filename="dadaab_s01e09.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.DADAAB_S01E10,
                           coded_field="rqa_s01e10_coded",
                           analysis_file_key="rqa_s01e10_",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.DADAAB_S01E10, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.DADAAB_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("covid19 adaptation dadaab s01e10"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),
    ]

    KAKUMA_RQA_CODING_PLANS = [
        CodingPlan(raw_field="rqa_s01e01_raw",
                   dataset_name="kakuma_s01e01",
                   time_field="sent_on",
                   run_id_field="rqa_s01e01_run_id",
                   coda_filename="kakuma_s01e01.json",
                   icr_filename="kakuma_s01e01.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.KAKUMA_S01E01,
                           coded_field="rqa_s01e01_coded",
                           analysis_file_key="rqa_s01e01_",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.KAKUMA_S01E01, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.KAKUMA_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("covid19 adaptation kakuma s01e01"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_s01e02_raw",
                   dataset_name="kakuma_s01e02",
                   time_field="sent_on",
                   run_id_field="rqa_s01e02_run_id",
                   coda_filename="kakuma_s01e02.json",
                   icr_filename="kakuma_s01e02.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.KAKUMA_S01E02,
                           coded_field="rqa_s01e02_coded",
                           analysis_file_key="rqa_s01e02_",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.KAKUMA_S01E02, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.KAKUMA_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("covid19 adaptation kakuma s01e02"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_s01e03_raw",
                   dataset_name="kakuma_s01e03",
                   time_field="sent_on",
                   run_id_field="rqa_s01e03_run_id",
                   coda_filename="kakuma_s01e03.json",
                   icr_filename="kakuma_s01e03.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.KAKUMA_S01E03,
                           coded_field="rqa_s01e03_coded",
                           analysis_file_key="rqa_s01e03_",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.KAKUMA_S01E03, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.KAKUMA_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("covid19 adaptation kakuma s01e03"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_s01e04_raw",
                   dataset_name="kakuma_s01e04",
                   time_field="sent_on",
                   run_id_field="rqa_s01e04_run_id",
                   coda_filename="kakuma_s01e04.json",
                   icr_filename="kakuma_s01e04.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.KAKUMA_S01E04,
                           coded_field="rqa_s01e04_coded",
                           analysis_file_key="rqa_s01e04_",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.KAKUMA_S01E04, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.KAKUMA_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("covid19 adaptation kakuma s01e04"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_s01e05_raw",
                   dataset_name="kakuma_s01e05",
                   time_field="sent_on",
                   run_id_field="rqa_s01e05_run_id",
                   coda_filename="kakuma_s01e05.json",
                   icr_filename="kakuma_s01e05.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.KAKUMA_S01E05,
                           coded_field="rqa_s01e05_coded",
                           analysis_file_key="rqa_s01e05_",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.KAKUMA_S01E05, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.KAKUMA_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("covid19 adaptation kakuma s01e05"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_s01e06_raw",
                   dataset_name="kakuma_s01e06",
                   time_field="sent_on",
                   run_id_field="rqa_s01e06_run_id",
                   coda_filename="kakuma_s01e06.json",
                   icr_filename="kakuma_s01e06.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.KAKUMA_S01E06,
                           coded_field="rqa_s01e06_coded",
                           analysis_file_key="rqa_s01e06_",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.KAKUMA_S01E06, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.KAKUMA_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("covid19 adaptation kakuma s01e06"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_s01e07_raw",
                   dataset_name="kakuma_s01e07",
                   time_field="sent_on",
                   run_id_field="rqa_s01e07_run_id",
                   coda_filename="kakuma_s01e07.json",
                   icr_filename="kakuma_s01e07.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.KAKUMA_S01E07,
                           coded_field="rqa_s01e07_coded",
                           analysis_file_key="rqa_s01e07_",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.KAKUMA_S01E07, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.KAKUMA_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("covid19 adaptation kakuma s01e07"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_s01e08_raw",
                   dataset_name="kakuma_s01e08",
                   time_field="sent_on",
                   run_id_field="rqa_s01e08_run_id",
                   coda_filename="kakuma_s01e08.json",
                   icr_filename="kakuma_s01e08.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.KAKUMA_S01E08,
                           coded_field="rqa_s01e08_coded",
                           analysis_file_key="rqa_s01e08_",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.KAKUMA_S01E08, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.KAKUMA_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("covid19 adaptation kakuma s01e08"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_s01e09_raw",
                   dataset_name="kakuma_s01e09",
                   time_field="sent_on",
                   run_id_field="rqa_s01e09_run_id",
                   coda_filename="kakuma_s01e09.json",
                   icr_filename="kakuma_s01e09.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.KAKUMA_S01E09,
                           coded_field="rqa_s01e09_coded",
                           analysis_file_key="rqa_s01e09_",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.KAKUMA_S01E09, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.KAKUMA_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("covid19 adaptation kakuma s01e09"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_s01e10_raw",
                   dataset_name="kakuma_s01e10",
                   time_field="sent_on",
                   run_id_field="rqa_s01e10_run_id",
                   coda_filename="kakuma_s01e10.json",
                   icr_filename="kakuma_s01e10.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.KAKUMA_S01E10,
                           coded_field="rqa_s01e10_coded",
                           analysis_file_key="rqa_s01e10_",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.KAKUMA_S01E10, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.KAKUMA_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("covid19 adaptation kakuma s01e10"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),
    ]

    @staticmethod
    def clean_age_with_range_filter(text):
        """
        Cleans age from the given `text`, setting to NC if the cleaned age is not in the range 10 <= age < 100.
        """
        age = swahili.DemographicCleaner.clean_age(text)
        if type(age) == int and 10 <= age < 100:
            return str(age)
            # TODO: Once the cleaners are updated to not return Codes.NOT_CODED, this should be updated to still return
            #       NC in the case where age is an int but is out of range
        else:
            return Codes.NOT_CODED

    SURVEY_CODING_PLANS = None

    KAKUMA_DEMOG_CODING_PLANS = [

        CodingPlan(raw_field="location_raw",
                   dataset_name="kakuma_location",
                   time_field="location_time",
                   coda_filename="kakuma_location.json",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.KAKUMA_LOCATION,
                           coded_field="location_coded",
                           analysis_file_key="location",
                           fold_strategy=FoldStrategies.assert_label_ids_equal
                       ),
                   ],
                   ws_code=CodeSchemes.KAKUMA_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("kakuma location"),
                   raw_field_fold_strategy=FoldStrategies.assert_equal),

        CodingPlan(raw_field="gender_raw",
                   dataset_name="kakuma_gender",
                   time_field="gender_time",
                   coda_filename="kakuma_gender.json",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.GENDER,
                           cleaner=somali.DemographicCleaner.clean_gender,
                           coded_field="gender_coded",
                           analysis_file_key="gender",
                           fold_strategy=FoldStrategies.assert_label_ids_equal
                       )
                   ],
                   ws_code=CodeSchemes.KAKUMA_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("kakuma gender"),
                   raw_field_fold_strategy=FoldStrategies.assert_equal),

        CodingPlan(raw_field="age_raw",
                   dataset_name="kakuma_age",
                   time_field="age_time",
                   coda_filename="kakuma_age.json",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.AGE,
                           cleaner=lambda text: PipelineConfiguration.clean_age_with_range_filter(text),
                           coded_field="age_coded",
                           analysis_file_key="age",
                           fold_strategy=FoldStrategies.assert_label_ids_equal
                       ),
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.AGE_CATEGORY,
                           coded_field="age_category_coded",
                           analysis_file_key="age_category",
                           fold_strategy=FoldStrategies.assert_label_ids_equal
                       )
                   ],
                   code_imputation_function=code_imputation_functions.impute_age_category,
                   ws_code=CodeSchemes.KAKUMA_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("kakuma age"),
                   raw_field_fold_strategy=FoldStrategies.assert_equal),

        CodingPlan(raw_field="household_language_raw",
                   dataset_name="kakuma_household_language",
                   time_field="household_language_time",
                   coda_filename="kakuma_household_language.json",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.KAKUMA_HOUSEHOLD_LANGUAGE,
                           coded_field="household_language_coded",
                           analysis_file_key="household_language",
                           fold_strategy=FoldStrategies.assert_label_ids_equal
                       )
                   ],
                   ws_code=CodeSchemes.KAKUMA_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("kakuma household language"),
                   raw_field_fold_strategy=FoldStrategies.assert_equal),

        CodingPlan(raw_field="nationality_raw",
                   dataset_name="kakuma_nationality",
                   time_field="nationality_time",
                   coda_filename="kakuma_nationality.json",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.NATIONALITY,
                           coded_field="nationality_coded",
                           analysis_file_key="nationality",
                           fold_strategy=FoldStrategies.assert_label_ids_equal
                       )
                   ],
                   ws_code=CodeSchemes.KAKUMA_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("kakuma nationality"),
                   raw_field_fold_strategy=FoldStrategies.assert_equal),
    ]

    KAKUMA_FOLLOW_UP_SURVEY_CODING_PLANS = [
        CodingPlan(raw_field="learning_from_home_experience_raw",
                   dataset_name="kakuma_learning_from_home_experience",
                   time_field="learning_from_home_experience_time",
                   coda_filename="kakuma_learning_from_home_experience.json",
                   icr_filename="kakuma_learning_from_home_experience.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.KAKUMA_LEARNING_FROM_HOME_EXPERIENCE,
                           coded_field="kakuma_learning_from_home_experience_coded",
                           analysis_file_key="kakuma_learning_from_home_experience_",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.KAKUMA_LEARNING_FROM_HOME_EXPERIENCE, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.KAKUMA_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value(
                       "covid19 adaptation kakuma learning from home experience"),
                   raw_field_fold_strategy=FoldStrategies.concatenate)
    ]

    KAKUMA_SURVEY_CODING_PLANS = KAKUMA_DEMOG_CODING_PLANS + KAKUMA_FOLLOW_UP_SURVEY_CODING_PLANS

    DADAAB_DEMOG_CODING_PLANS = [

        CodingPlan(raw_field="location_raw",
                   dataset_name="dadaab_location",
                   time_field="location_time",
                   coda_filename="dadaab_location.json",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.DADAAB_LOCATION,
                           coded_field="location_coded",
                           analysis_file_key="location",
                           fold_strategy=FoldStrategies.assert_label_ids_equal
                       ),
                   ],
                   ws_code=CodeSchemes.DADAAB_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("dadaab location"),
                   raw_field_fold_strategy=FoldStrategies.assert_equal),

        CodingPlan(raw_field="gender_raw",
                   dataset_name="dadaab_gender",
                   time_field="gender_time",
                   coda_filename="dadaab_gender.json",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.GENDER,
                           cleaner=somali.DemographicCleaner.clean_gender,
                           coded_field="gender_coded",
                           analysis_file_key="gender",
                           fold_strategy=FoldStrategies.assert_label_ids_equal
                       )
                   ],
                   ws_code=CodeSchemes.DADAAB_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("dadaab gender"),
                   raw_field_fold_strategy=FoldStrategies.assert_equal),

        CodingPlan(raw_field="age_raw",
                   dataset_name="dadaab_age",
                   time_field="age_time",
                   coda_filename="dadaab_age.json",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.AGE,
                           cleaner=lambda text: PipelineConfiguration.clean_age_with_range_filter(text),
                           coded_field="age_coded",
                           analysis_file_key="age",
                           fold_strategy=FoldStrategies.assert_label_ids_equal
                       ),
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.AGE_CATEGORY,
                           coded_field="age_category_coded",
                           analysis_file_key="age_category",
                           fold_strategy=FoldStrategies.assert_label_ids_equal
                       )
                   ],
                   code_imputation_function=code_imputation_functions.impute_age_category,
                   ws_code=CodeSchemes.DADAAB_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("dadaab age"),
                   raw_field_fold_strategy=FoldStrategies.assert_equal),

        CodingPlan(raw_field="household_language_raw",
                   dataset_name="dadaab_household_language",
                   time_field="household_language_time",
                   coda_filename="dadaab_household_language.json",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.DADAAB_HOUSEHOLD_LANGUAGE,
                           coded_field="household_language_coded",
                           analysis_file_key="household_language",
                           fold_strategy=FoldStrategies.assert_label_ids_equal
                       )
                   ],
                   ws_code=CodeSchemes.DADAAB_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("dadaab household language"),
                   raw_field_fold_strategy=FoldStrategies.assert_equal),

        CodingPlan(raw_field="nationality_raw",
                   dataset_name="dadaab_nationality",
                   time_field="nationality_time",
                   coda_filename="dadaab_nationality.json",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.NATIONALITY,
                           coded_field="nationality_coded",
                           analysis_file_key="nationality",
                           fold_strategy=FoldStrategies.assert_label_ids_equal
                       )
                   ],
                   ws_code=CodeSchemes.DADAAB_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value("dadaab nationality"),
                   raw_field_fold_strategy=FoldStrategies.assert_equal),
    ]

    DADAAB_FOLLOW_UP_SURVEY_CODING_PLANS = [
        CodingPlan(raw_field="learning_from_home_experience_raw",
                   dataset_name="dadaab_learning_from_home_experience",
                   time_field="learning_from_home_experience_time",
                   coda_filename="dadaab_learning_from_home_experience.json",
                   icr_filename="dadaab_learning_from_home_experience.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.DADAAB_LEARNING_FROM_HOME_EXPERIENCE,
                           coded_field="dadaab_learning_from_home_experience_coded",
                           analysis_file_key="dadaab_learning_from_home_experience_",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(
                               CodeSchemes.DADAAB_LEARNING_FROM_HOME_EXPERIENCE, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.DADAAB_WS_CORRECT_DATASET_SCHEME.get_code_with_match_value(
                       "covid19 adaptation dadaab learning from home experience"),
                   raw_field_fold_strategy=FoldStrategies.concatenate)
    ]

    DADAAB_SURVEY_CODING_PLANS = DADAAB_DEMOG_CODING_PLANS + DADAAB_FOLLOW_UP_SURVEY_CODING_PLANS

    def __init__(self, pipeline_name, raw_data_sources, phone_number_uuid_table, timestamp_remappings,
                 rapid_pro_key_remappings, project_start_date, project_end_date, filter_test_messages, move_ws_messages,
                 memory_profile_upload_bucket, data_archive_upload_bucket, bucket_dir_path, drive_upload=None):
        """
        :param pipeline_name: The name of this pipeline.
        :type pipeline_name: str
        :param raw_data_sources: List of sources to pull the various raw run files from.
        :type raw_data_sources: list of RawDataSource
        :param phone_number_uuid_table: Configuration for the Firestore phone number <-> uuid table.
        :type phone_number_uuid_table: PhoneNumberUuidTable
        :param rapid_pro_key_remappings: List of rapid_pro_key -> pipeline_key remappings.
        :type rapid_pro_key_remappings: list of RapidProKeyRemapping
        :param project_start_date: When data collection started - all activation messages received before this date
                                   time will be dropped.
        :type project_start_date: datetime.datetime
        :param project_end_date: When data collection stopped - all activation messages received on or after this date
                                 time will be dropped.
        :type project_end_date: datetime.datetime
        :param filter_test_messages: Whether to filter out messages sent from the rapid_pro_test_contact_uuids
        :type filter_test_messages: bool
        :param move_ws_messages: Whether to move messages labelled as Wrong Scheme to the correct dataset.
        :type move_ws_messages: bool
        :param memory_profile_upload_bucket: The GS bucket name to upload the memory profile log to.
                                              This name will be appended with the log_dir_path
                                              and the file basename to generate the log upload location.
        :type memory_profile_upload_bucket: str
        :param data_archive_upload_bucket: The GS bucket name to upload the data archive file to.
                                            This name will be appended with the log_dir_path
                                            and the file basename to generate the archive upload location.
        :type data_archive_upload_bucket: str
        :param bucket_dir_path: The GS bucket folder path to store the data archive & memory log files to.
        :type bucket_dir_path: str
        :param drive_upload: Configuration for uploading to Google Drive, or None.
                             If None, does not upload to Google Drive.
        :type drive_upload: DriveUploadPaths | None
        """
        self.pipeline_name = pipeline_name
        self.raw_data_sources = raw_data_sources
        self.phone_number_uuid_table = phone_number_uuid_table
        self.timestamp_remappings = timestamp_remappings
        self.rapid_pro_key_remappings = rapid_pro_key_remappings
        self.project_start_date = project_start_date
        self.project_end_date = project_end_date
        self.filter_test_messages = filter_test_messages
        self.move_ws_messages = move_ws_messages
        self.drive_upload = drive_upload
        self.memory_profile_upload_bucket = memory_profile_upload_bucket
        self.data_archive_upload_bucket = data_archive_upload_bucket
        self.bucket_dir_path = bucket_dir_path
        self.validate()

    @classmethod
    def from_configuration_dict(cls, configuration_dict):
        pipeline_name = configuration_dict["PipelineName"]

        raw_data_sources = []
        for raw_data_source in configuration_dict["RawDataSources"]:
            if raw_data_source["SourceType"] == "RapidPro":
                raw_data_sources.append(RapidProSource.from_configuration_dict(raw_data_source))
            else:
                assert False, f"Unknown SourceType '{raw_data_source['SourceType']}'. " \
                    f"Must be 'RapidPro'"

        phone_number_uuid_table = PhoneNumberUuidTable.from_configuration_dict(
            configuration_dict["PhoneNumberUuidTable"])

        timestamp_remappings = []
        for remapping_dict in configuration_dict.get("TimestampRemappings", []):
            timestamp_remappings.append(TimestampRemapping.from_configuration_dict(remapping_dict))

        rapid_pro_key_remappings = []
        for remapping_dict in configuration_dict["RapidProKeyRemappings"]:
            rapid_pro_key_remappings.append(RapidProKeyRemapping.from_configuration_dict(remapping_dict))

        project_start_date = isoparse(configuration_dict["ProjectStartDate"])
        project_end_date = isoparse(configuration_dict["ProjectEndDate"])

        filter_test_messages = configuration_dict["FilterTestMessages"]
        move_ws_messages = configuration_dict["MoveWSMessages"]

        drive_upload_paths = None
        if "DriveUpload" in configuration_dict:
            drive_upload_paths = DriveUpload.from_configuration_dict(configuration_dict["DriveUpload"])

        memory_profile_upload_bucket = configuration_dict["MemoryProfileUploadBucket"]
        data_archive_upload_bucket = configuration_dict["DataArchiveUploadBucket"]
        bucket_dir_path = configuration_dict["BucketDirPath"]

        return cls(pipeline_name, raw_data_sources, phone_number_uuid_table, timestamp_remappings,
                   rapid_pro_key_remappings, project_start_date, project_end_date, filter_test_messages,
                   move_ws_messages, memory_profile_upload_bucket, data_archive_upload_bucket, bucket_dir_path,
                   drive_upload_paths)

    @classmethod
    def from_configuration_file(cls, f):
        return cls.from_configuration_dict(json.load(f))

    def validate(self):
        validators.validate_string(self.pipeline_name, "pipeline_name")

        validators.validate_list(self.raw_data_sources, "raw_data_sources")
        for i, raw_data_source in enumerate(self.raw_data_sources):
            assert isinstance(raw_data_source, RawDataSource), f"raw_data_sources[{i}] is not of type of RawDataSource"
            raw_data_source.validate()

        assert isinstance(self.phone_number_uuid_table, PhoneNumberUuidTable)
        self.phone_number_uuid_table.validate()

        validators.validate_list(self.rapid_pro_key_remappings, "rapid_pro_key_remappings")
        for i, remapping in enumerate(self.rapid_pro_key_remappings):
            assert isinstance(remapping, RapidProKeyRemapping), \
                f"rapid_pro_key_mappings[{i}] is not of type RapidProKeyRemapping"
            remapping.validate()

        validators.validate_datetime(self.project_start_date, "project_start_date")
        validators.validate_datetime(self.project_end_date, "project_end_date")

        validators.validate_bool(self.filter_test_messages, "filter_test_messages")
        validators.validate_bool(self.move_ws_messages, "move_ws_messages")

        if self.drive_upload is not None:
            assert isinstance(self.drive_upload, DriveUpload), \
                "drive_upload is not of type DriveUpload"
            self.drive_upload.validate()

        validators.validate_url(self.memory_profile_upload_bucket, "memory_profile_upload_bucket", "gs")
        validators.validate_url(self.data_archive_upload_bucket, "data_archive_upload_bucket", "gs")
        validators.validate_string(self.bucket_dir_path, "bucket_dir_path")


class RawDataSource(ABC):
    @abstractmethod
    def get_activation_flow_names(self):
        pass

    @abstractmethod
    def get_survey_flow_names(self):
        pass

    @abstractmethod
    def validate(self):
        pass


class RapidProSource(RawDataSource):
    def __init__(self, domain, token_file_url, contacts_file_name, activation_flow_names, survey_flow_names,
                 test_contact_uuids):
        """
        :param domain: URL of the Rapid Pro server to download data from.
        :type domain: str
        :param token_file_url: GS URL of a text file containing the authorisation token for the Rapid Pro server.
        :type token_file_url: str
        :param contacts_file_name:
        :type contacts_file_name: str
        :param activation_flow_names: The names of the RapidPro flows that contain the radio show responses.
        :type: activation_flow_names: list of str
        :param survey_flow_names: The names of the RapidPro flows that contain the survey responses.
        :type: survey_flow_names: list of str
        :param test_contact_uuids: Rapid Pro contact UUIDs of test contacts.
                                   Runs for any of those test contacts will be tagged with {'test_run': True},
                                   and dropped when the pipeline is run with "FilterTestMessages" set to true.
        :type test_contact_uuids: list of str
        """
        self.domain = domain
        self.token_file_url = token_file_url
        self.contacts_file_name = contacts_file_name
        self.activation_flow_names = activation_flow_names
        self.survey_flow_names = survey_flow_names
        self.test_contact_uuids = test_contact_uuids

        self.validate()

    def get_activation_flow_names(self):
        return self.activation_flow_names

    def get_survey_flow_names(self):
        return self.survey_flow_names

    @classmethod
    def from_configuration_dict(cls, configuration_dict):
        domain = configuration_dict["Domain"]
        token_file_url = configuration_dict["TokenFileURL"]
        contacts_file_name = configuration_dict["ContactsFileName"]
        activation_flow_names = configuration_dict.get("ActivationFlowNames", [])
        survey_flow_names = configuration_dict.get("SurveyFlowNames", [])
        test_contact_uuids = configuration_dict.get("TestContactUUIDs", [])

        return cls(domain, token_file_url, contacts_file_name, activation_flow_names,
                   survey_flow_names, test_contact_uuids)

    def validate(self):
        validators.validate_string(self.domain, "domain")
        validators.validate_string(self.token_file_url, "token_file_url")
        validators.validate_string(self.contacts_file_name, "contacts_file_name")

        validators.validate_list(self.activation_flow_names, "activation_flow_names")
        for i, activation_flow_name in enumerate(self.activation_flow_names):
            validators.validate_string(activation_flow_name, f"activation_flow_names[{i}]")

        validators.validate_list(self.survey_flow_names, "survey_flow_names")
        for i, survey_flow_name in enumerate(self.survey_flow_names):
            validators.validate_string(survey_flow_name, f"survey_flow_names[{i}]")

        validators.validate_list(self.test_contact_uuids, "test_contact_uuids")
        for i, contact_uuid in enumerate(self.test_contact_uuids):
            validators.validate_string(contact_uuid, f"test_contact_uuids[{i}]")


class AbstractRemoteURLSource(RawDataSource):
    def __init__(self, activation_flow_urls, survey_flow_urls):
        self.activation_flow_urls = activation_flow_urls
        self.survey_flow_urls = survey_flow_urls

        self.validate()

    def get_activation_flow_names(self):
        return [url.split('/')[-1].split('.')[0] for url in self.activation_flow_urls]

    def get_survey_flow_names(self):
        return [url.split('/')[-1].split('.')[0] for url in self.survey_flow_urls]

    @classmethod
    def from_configuration_dict(cls, configuration_dict):
        activation_flow_urls = configuration_dict.get("ActivationFlowURLs", [])
        survey_flow_urls = configuration_dict.get("SurveyFlowURLs", [])

        return cls(activation_flow_urls, survey_flow_urls)

    def validate(self):
        validators.validate_list(self.activation_flow_urls, "activation_flow_urls")
        for i, activation_flow_url in enumerate(self.activation_flow_urls):
            validators.validate_url(activation_flow_url, f"activation_flow_urls[{i}]", "gs")

        validators.validate_list(self.survey_flow_urls, "survey_flow_urls")
        for i, survey_flow_url in enumerate(self.survey_flow_urls):
            validators.validate_url(survey_flow_url, f"survey_flow_urls[{i}]", "gs")


class PhoneNumberUuidTable(object):
    def __init__(self, firebase_credentials_file_url, table_name):
        """
        :param firebase_credentials_file_url: GS URL to the private credentials file for the Firebase account where
                                                 the phone number <-> uuid table is stored.
        :type firebase_credentials_file_url: str
        :param table_name: Name of the data <-> uuid table in Firebase to use.
        :type table_name: str
        """
        self.firebase_credentials_file_url = firebase_credentials_file_url
        self.table_name = table_name

        self.validate()

    @classmethod
    def from_configuration_dict(cls, configuration_dict):
        firebase_credentials_file_url = configuration_dict["FirebaseCredentialsFileURL"]
        table_name = configuration_dict["TableName"]

        return cls(firebase_credentials_file_url, table_name)

    def validate(self):
        validators.validate_url(self.firebase_credentials_file_url, "firebase_credentials_file_url", scheme="gs")
        validators.validate_string(self.table_name, "table_name")


class TimestampRemapping(object):
    def __init__(self, time_key, show_pipeline_key_to_remap_to, range_start_inclusive=None, range_end_exclusive=None,
                 time_to_adjust_to=None):
        """
        Specifies a remapping of messages received within the given time range to another radio show field.
        Optionally specifies an adjustment of all affected timestamps to a constant datetime.

        :param time_key: Key in each TracedData of an ISO 8601-formatted datetime string to read the message sent on
                         time from.
        :type time_key: str
        :param show_pipeline_key_to_remap_to: Pipeline key to assign to messages received within the given time range.
        :type show_pipeline_key_to_remap_to: str
        :param range_start_inclusive: Start datetime for the time range to remap radio show messages from, inclusive.
                                      If None, defaults to the beginning of time.
        :type range_start_inclusive: datetime | None
        :param range_end_exclusive: End datetime for the time range to remap radio show messages from, exclusive.
                                    If None, defaults to the end of time.
        :type range_end_exclusive: datetime | None
        :param time_to_adjust_to: Datetime to adjust each message object's `time_key` field to, or None.
                                  If None, re-mapped shows will not have timestamps adjusted.
        :type time_to_adjust_to: datetime | None
        """
        if range_start_inclusive is None:
            range_start_inclusive = pytz.utc.localize(datetime.min)
        if range_end_exclusive is None:
            range_end_exclusive = pytz.utc.localize(datetime.max)

        self.time_key = time_key
        self.show_pipeline_key_to_remap_to = show_pipeline_key_to_remap_to
        self.range_start_inclusive = range_start_inclusive
        self.range_end_exclusive = range_end_exclusive
        self.time_to_adjust_to = time_to_adjust_to

        self.validate()

    @classmethod
    def from_configuration_dict(cls, configuration_dict):
        time_key = configuration_dict["TimeKey"]
        show_pipeline_key_to_remap_to = configuration_dict["ShowPipelineKeyToRemapTo"]
        range_start_inclusive = configuration_dict.get("RangeStartInclusive")
        range_end_exclusive = configuration_dict.get("RangeEndExclusive")
        time_to_adjust_to = configuration_dict.get("TimeToAdjustTo")

        if range_start_inclusive is not None:
            range_start_inclusive = isoparse(range_start_inclusive)
        if range_end_exclusive is not None:
            range_end_exclusive = isoparse(range_end_exclusive)
        if time_to_adjust_to is not None:
            time_to_adjust_to = isoparse(time_to_adjust_to)

        return cls(time_key, show_pipeline_key_to_remap_to, range_start_inclusive, range_end_exclusive,
                   time_to_adjust_to)

    def validate(self):
        validators.validate_string(self.time_key, "time_key")
        validators.validate_string(self.show_pipeline_key_to_remap_to, "show_pipeline_key_to_remap_to")
        validators.validate_datetime(self.range_start_inclusive, "range_start_inclusive")
        validators.validate_datetime(self.range_end_exclusive, "range_end_exclusive")

        if self.time_to_adjust_to is not None:
            validators.validate_datetime(self.time_to_adjust_to, "time_to_adjust_to")


class RapidProKeyRemapping(object):
    def __init__(self, is_activation_message, rapid_pro_key, pipeline_key):
        """
        :param is_activation_message: Whether this re-mapping contains an activation message (activation messages need
                                   to be handled differently because they are not always in the correct flow)
        :type is_activation_message: bool
        :param rapid_pro_key: Name of key in the dataset exported via RapidProTools.
        :type rapid_pro_key: str
        :param pipeline_key: Name to use for that key in the rest of the pipeline.
        :type pipeline_key: str
        """
        self.is_activation_message = is_activation_message
        self.rapid_pro_key = rapid_pro_key
        self.pipeline_key = pipeline_key

        self.validate()

    @classmethod
    def from_configuration_dict(cls, configuration_dict):
        is_activation_message = configuration_dict.get("IsActivationMessage", False)
        rapid_pro_key = configuration_dict["RapidProKey"]
        pipeline_key = configuration_dict["PipelineKey"]

        return cls(is_activation_message, rapid_pro_key, pipeline_key)

    def validate(self):
        validators.validate_bool(self.is_activation_message, "is_activation_message")
        validators.validate_string(self.rapid_pro_key, "rapid_pro_key")
        validators.validate_string(self.pipeline_key, "pipeline_key")


class DriveUpload(object):
    def __init__(self, drive_credentials_file_url, production_upload_path, messages_upload_path,
                 individuals_upload_path, automated_analysis_dir):
        """
        :param drive_credentials_file_url: GS URL to the private credentials file for the Drive service account to use
                                           to upload the output files.
        :type drive_credentials_file_url: str
        :param production_upload_path: Path in the Drive service account's "Shared with Me" directory to upload the
                                       production CSV to.
        :type production_upload_path: str
        :param messages_upload_path: Path in the Drive service account's "Shared with Me" directory to upload the
                                     messages analysis CSV to.
        :type messages_upload_path: str
        :param individuals_upload_path: Path in the Drive service account's "Shared with Me" directory to upload the
                                        individuals analysis CSV to.
        :type individuals_upload_path: str
        :param automated_analysis_dir: Directory in the Drive service account's "Shared with Me" directory to upload the
                                    automated analysis files from this pipeline run to.
        :type automated_analysis_dir: str
        """
        self.drive_credentials_file_url = drive_credentials_file_url
        self.production_upload_path = production_upload_path
        self.messages_upload_path = messages_upload_path
        self.individuals_upload_path = individuals_upload_path
        self.automated_analysis_dir = automated_analysis_dir

        self.validate()

    @classmethod
    def from_configuration_dict(cls, configuration_dict):
        drive_credentials_file_url = configuration_dict["DriveCredentialsFileURL"]
        production_upload_path = configuration_dict["ProductionUploadPath"]
        messages_upload_path = configuration_dict["MessagesUploadPath"]
        individuals_upload_path = configuration_dict["IndividualsUploadPath"]
        automated_analysis_dir = configuration_dict["AutomatedAnalysisDir"]

        return cls(drive_credentials_file_url, production_upload_path, messages_upload_path,
                   individuals_upload_path, automated_analysis_dir)

    def validate(self):
        validators.validate_string(self.drive_credentials_file_url, "drive_credentials_file_url")
        assert urlparse(self.drive_credentials_file_url).scheme == "gs", "DriveCredentialsFileURL needs to be a gs " \
                                                                         "URL (i.e. of the form gs://bucket-name/file)"

        validators.validate_string(self.production_upload_path, "production_upload_path")
        validators.validate_string(self.messages_upload_path, "messages_upload_path")
        validators.validate_string(self.individuals_upload_path, "individuals_upload_path")
        validators.validate_string(self.automated_analysis_dir, "automated_analysis_dir")
