import json

from core_data_modules.data_models import CodeScheme


def _open_scheme(filename):
    with open(f"code_schemes/{filename}", "r") as f:
        firebase_map = json.load(f)
        return CodeScheme.from_firebase_map(firebase_map)


class CodeSchemes(object):
    DADAAB_S01E01 = _open_scheme("dadaab_s01e01.json")
    DADAAB_S01E02 = _open_scheme("dadaab_s01e02.json")
    DADAAB_S01E03 = _open_scheme("dadaab_s01e03.json")
    DADAAB_S01E04 = _open_scheme("dadaab_s01e04.json")
    DADAAB_S01E05 = _open_scheme("dadaab_s01e05.json")
    DADAAB_S01E06 = _open_scheme("dadaab_s01e06.json")
    DADAAB_S01E07 = _open_scheme("dadaab_s01e07.json")
    DADAAB_S01E08 = _open_scheme("dadaab_s01e08.json")
    DADAAB_S01E09 = _open_scheme("dadaab_s01e09.json")
    DADAAB_S01E10 = _open_scheme("dadaab_s01e10.json")

    KAKUMA_S01E01 = _open_scheme("kakuma_s01e01.json")
    KAKUMA_S01E02 = _open_scheme("kakuma_s01e02.json")
    KAKUMA_S01E03 = _open_scheme("kakuma_s01e03.json")
    KAKUMA_S01E04 = _open_scheme("kakuma_s01e04.json")
    KAKUMA_S01E05 = _open_scheme("kakuma_s01e05.json")
    KAKUMA_S01E06 = _open_scheme("kakuma_s01e06.json")
    KAKUMA_S01E07 = _open_scheme("kakuma_s01e07.json")
    KAKUMA_S01E08 = _open_scheme("kakuma_s01e08.json")
    KAKUMA_S01E09 = _open_scheme("kakuma_s01e09.json")
    KAKUMA_S01E10 = _open_scheme("kakuma_s01e10.json")

    GENDER = _open_scheme("gender.json")
    NATIONALITY = _open_scheme("nationality.json")
    AGE = _open_scheme("age.json")
    AGE_CATEGORY = _open_scheme("age_category.json")
    DADAAB_HOUSEHOLD_LANGUAGE = _open_scheme("dadaab_household_language.json") # We have different language & location schemes for the two camps
    DADAAB_LOCATION = _open_scheme("dadaab_location.json")
    KAKUMA_HOUSEHOLD_LANGUAGE = _open_scheme("kakuma_household_language.json")
    KAKUMA_LOCATION = _open_scheme("kakuma_location.json")

    WS_CORRECT_DATASET_SCHEME = None
    KAKUMA_WS_CORRECT_DATASET_SCHEME = _open_scheme("kakuma_ws_correct_dataset.json")
    DADAAB_WS_CORRECT_DATASET_SCHEME = _open_scheme("dadaab_ws_correct_dataset.json")
