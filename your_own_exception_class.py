# You can write your own exception classes
# So that others will be able to easily understand what the error means
class BaseValidationError(ValueError):
    pass

class NumInputTooSmallError(BaseValidationError):
    pass

class NumInputNeedsToBeNumType(BaseValidationError):
    pass

def validate(num):
    if not isinstance(num, (int, float)):
        raise NumInputNeedsToBeNumType
    if num < 10:
        raise NumInputTooSmallError

validate(7) 
# validate('a')
