from app.models.error_model import MissingKeyError, WrongKeysError


class Check:
    @staticmethod
    def keys(expected_keys, keys, is_updating=False):

        wrong_keys = [key for key in keys if not key in expected_keys]
        missing_keys = [key for key in expected_keys if not key in keys]

        if len(wrong_keys) > 0:
            raise WrongKeysError(wrong_keys)

        if len(missing_keys) > 0 and not is_updating:
            raise MissingKeyError(missing_keys)
