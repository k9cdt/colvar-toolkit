import cvtoolkit
from cvtoolkit import Colvar
import pytest
import numpy as np

from helpers import *

def test_read_method():
    cv = cvtoolkit.read(BASE_COLVAR)
    assert cv is not None
    assert cv._data.shape == (DAT_COL, DAT_LENGTH)
    assert cv.header == cv._header
    check_reproduce(cv)

