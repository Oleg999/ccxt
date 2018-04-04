import os
import sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root)

# --------------------------------------------------------------------------------------------------------

from ccxt.base.decimal_to_precision import decimal_to_precision  # noqa F401
from ccxt.base.decimal_to_precision import TRUNCATE              # noqa F401
from ccxt.base.decimal_to_precision import ROUND                 # noqa F401
from ccxt.base.decimal_to_precision import DECIMAL_PLACES        # noqa F401
from ccxt.base.decimal_to_precision import SIGNIFICANT_DIGITS    # noqa F401
from ccxt.base.decimal_to_precision import PAD_WITH_ZERO         # noqa F401
from ccxt.base.decimal_to_precision import NO_PADDING            # noqa F401

# --------------------------------------------------------------------------------------------------------

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

# --------------------------------------------------------------------------------------------------------
# testDecimalToPrecisionTruncationToNDigitsAfterDot

assert decimal_to_precision('12.3456000', TRUNCATE, 10, DECIMAL_PLACES, NO_PADDING) == '12.3456'
assert decimal_to_precision('12.3456', TRUNCATE, 27, DECIMAL_PLACES, NO_PADDING) == '12.3456'
assert decimal_to_precision('12.3456', TRUNCATE, 4, DECIMAL_PLACES, NO_PADDING) == '12.3456'
assert decimal_to_precision('12.3456', TRUNCATE, 3, DECIMAL_PLACES, NO_PADDING) == '12.345'
assert decimal_to_precision('12.3456', TRUNCATE, 2, DECIMAL_PLACES, NO_PADDING) == '12.34'
assert decimal_to_precision('12.3456', TRUNCATE, 1, DECIMAL_PLACES, NO_PADDING) == '12.3'
assert decimal_to_precision('12.3456', TRUNCATE, 0, DECIMAL_PLACES, NO_PADDING) == '12'

# assert (Exchange::decimal_to_precision ('12.3456',    TRUNCATE,  -1, DECIMAL_PLACES) === '10');  // not supported yet
# assert (Exchange::decimal_to_precision ('123.456',    TRUNCATE,  -2, DECIMAL_PLACES) === '120'); // not supported yet
# assert (Exchange::decimal_to_precision ('123.456',    TRUNCATE,  -3, DECIMAL_PLACES) === '100'); // not supported yet

# --------------------------------------------------------------------------------------------------------
# testDecimalToPrecisionTruncationToNSignificantDigits

assert decimal_to_precision('0.000123456700', TRUNCATE, 27, SIGNIFICANT_DIGITS, NO_PADDING) == '0.0001234567'
assert decimal_to_precision('0.0001234567', TRUNCATE, 27, SIGNIFICANT_DIGITS, NO_PADDING) == '0.0001234567'
assert decimal_to_precision('0.0001234567', TRUNCATE, 7, SIGNIFICANT_DIGITS, NO_PADDING) == '0.0001234567'

assert decimal_to_precision('0.000123456', TRUNCATE, 6, SIGNIFICANT_DIGITS, NO_PADDING) == '0.000123456'
assert decimal_to_precision('0.00012345', TRUNCATE, 5, SIGNIFICANT_DIGITS, NO_PADDING) == '0.00012345'
assert decimal_to_precision('0.00012', TRUNCATE, 2, SIGNIFICANT_DIGITS, NO_PADDING) == '0.00012'
assert decimal_to_precision('0.0001', TRUNCATE, 1, SIGNIFICANT_DIGITS, NO_PADDING) == '0.0001'

assert decimal_to_precision('123.0000987654', TRUNCATE, 10, SIGNIFICANT_DIGITS, NO_PADDING) == '123.0000987'
assert decimal_to_precision('123.0000987654', TRUNCATE, 8, SIGNIFICANT_DIGITS, NO_PADDING) == '123.00009'
assert decimal_to_precision('123.0000987654', TRUNCATE, 7, SIGNIFICANT_DIGITS, NO_PADDING) == '123'
assert decimal_to_precision('123.0000987654', TRUNCATE, 7, SIGNIFICANT_DIGITS, PAD_WITH_ZERO) == '123.0000'
assert decimal_to_precision('123.0000987654', TRUNCATE, 4, SIGNIFICANT_DIGITS, PAD_WITH_ZERO) == '123.0'

assert decimal_to_precision('123.0000987654', TRUNCATE, 2, SIGNIFICANT_DIGITS, NO_PADDING) == '120'
assert decimal_to_precision('123.0000987654', TRUNCATE, 1, SIGNIFICANT_DIGITS, NO_PADDING) == '100'
assert decimal_to_precision('123.0000987654', TRUNCATE, 1, SIGNIFICANT_DIGITS, PAD_WITH_ZERO) == '100'

# --------------------------------------------------------------------------------------------------------
# testDecimalToPrecisionRoundingToNDigitsAfterDot

assert decimal_to_precision('12.3456000', ROUND, 27, DECIMAL_PLACES, NO_PADDING) == '12.3456'
assert decimal_to_precision('12.3456', ROUND, 27, DECIMAL_PLACES, NO_PADDING) == '12.3456'
assert decimal_to_precision('12.3456', ROUND, 4, DECIMAL_PLACES, NO_PADDING) == '12.3456'
assert decimal_to_precision('12.3456', ROUND, 3, DECIMAL_PLACES, NO_PADDING) == '12.346'
assert decimal_to_precision('12.3456', ROUND, 2, DECIMAL_PLACES, NO_PADDING) == '12.35'
assert decimal_to_precision('12.3456', ROUND, 1, DECIMAL_PLACES, NO_PADDING) == '12.3'
assert decimal_to_precision('12.3456', ROUND, 0, DECIMAL_PLACES, NO_PADDING) == '12'

# assert (Exchange::decimal_to_precision ('12.3456',    ROUND,  -1, DECIMAL_PLACES,    NO_PADDING,  '10');  // not supported yet
# assert (Exchange::decimal_to_precision ('123.456',    ROUND,  -1, DECIMAL_PLACES,    NO_PADDING,  '120'); // not supported yet
# assert (Exchange::decimal_to_precision ('123.456',    ROUND,  -2, DECIMAL_PLACES,    NO_PADDING,  '100'); // not supported yet

assert decimal_to_precision('9.999', ROUND, 3, DECIMAL_PLACES, NO_PADDING) == '9.999'
assert decimal_to_precision('9.999', ROUND, 2, DECIMAL_PLACES, NO_PADDING) == '10'
assert decimal_to_precision('9.999', ROUND, 2, DECIMAL_PLACES, PAD_WITH_ZERO) == '10.00'
assert decimal_to_precision('99.999', ROUND, 2, DECIMAL_PLACES, PAD_WITH_ZERO) == '100.00'
assert decimal_to_precision('-99.999', ROUND, 2, DECIMAL_PLACES, PAD_WITH_ZERO) == '-100.00'

# --------------------------------------------------------------------------------------------------------
# testDecimalToPrecisionRoundingToNSignificantDigits

assert decimal_to_precision('0.000123456700', ROUND, 27, SIGNIFICANT_DIGITS, NO_PADDING) == '0.0001234567'
assert decimal_to_precision('0.0001234567', ROUND, 27, SIGNIFICANT_DIGITS, NO_PADDING) == '0.0001234567'
assert decimal_to_precision('0.0001234567', ROUND, 7, SIGNIFICANT_DIGITS, NO_PADDING) == '0.0001234567'

assert decimal_to_precision('0.000123456', ROUND, 6, SIGNIFICANT_DIGITS, NO_PADDING) == '0.000123456'
assert decimal_to_precision('0.000123456', ROUND, 5, SIGNIFICANT_DIGITS, NO_PADDING) == '0.00012346'
assert decimal_to_precision('0.000123456', ROUND, 4, SIGNIFICANT_DIGITS, NO_PADDING) == '0.0001235'
assert decimal_to_precision('0.00012', ROUND, 2, SIGNIFICANT_DIGITS, NO_PADDING) == '0.00012'
assert decimal_to_precision('0.0001', ROUND, 1, SIGNIFICANT_DIGITS, NO_PADDING) == '0.0001'

assert decimal_to_precision('123.0000987654', ROUND, 7, SIGNIFICANT_DIGITS, NO_PADDING) == '123.0001'
assert decimal_to_precision('123.0000987654', ROUND, 6, SIGNIFICANT_DIGITS, NO_PADDING) == '123'

assert decimal_to_precision('0.00098765', ROUND, 2, SIGNIFICANT_DIGITS, NO_PADDING) == '0.00099'
assert decimal_to_precision('0.00098765', ROUND, 2, SIGNIFICANT_DIGITS, PAD_WITH_ZERO) == '0.00099'

assert decimal_to_precision('0.00098765', ROUND, 1, SIGNIFICANT_DIGITS, NO_PADDING) == '0.001'
assert decimal_to_precision('0.00098765', ROUND, 10, SIGNIFICANT_DIGITS, PAD_WITH_ZERO) == '0.0009876500000'

assert decimal_to_precision('0.098765', ROUND, 1, SIGNIFICANT_DIGITS, PAD_WITH_ZERO) == '0.1'

# --------------------------------------------------------------------------------------------------------
# testDecimalToPrecisionNegativeNumbers

assert decimal_to_precision('-0.123456', TRUNCATE, 5, DECIMAL_PLACES, NO_PADDING) == '-0.12345'
assert decimal_to_precision('-0.123456', ROUND, 5, DECIMAL_PLACES, NO_PADDING) == '-0.12346'
