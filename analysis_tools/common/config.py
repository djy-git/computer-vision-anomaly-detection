"""Configuration module

Commonly used constant parameters are defined in capital letters.
"""

# Author: Dongjin Yoon <djyoon0223@gmail.com>


### Common parameters
RANDOM_STATE = 42


### Plot parameters
SHOW_PLOT      = True
FIGSIZE_UNIT   = 5
FIGSIZE        = (5*FIGSIZE_UNIT, 3*FIGSIZE_UNIT)
BINS           = 50
N_CLASSES_PLOT = 5
N_COLS         = 5
LEARNING_CURVE_N_SUBSETS_STEP = 5


### Model selection
TEST_SIZE = 0.2


### Training
BATCH_SIZE = 32


### PATH
from os.path import join, dirname, abspath
class PATH:
    root   = abspath(dirname(dirname(dirname(__file__))))
    input  = join(root, 'open')
    output = join(root, 'output')
    result = join(root, 'result')
    train  = join(input, 'train')
    test   = join(input, 'test')
