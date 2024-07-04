# Testing PiPico W Training

[![codecov](https://codecov.io/gh/ikostan/pico/branch/master/graph/badge.svg?token=UV5L6GPUG8)](https://codecov.io/gh/ikostan/pico)

![Codecov Sunburst](https://codecov.io/gh/ikostan/pico/graphs/sunburst.svg?token=UV5L6GPUG8)

**Sunburst:** the inner-most circle is the entire project, moving away 
from the center are folders then, finally, a single file. The size and 
color of each slice is representing the number of statements and the 
coverage, respectively.

[What percentage of coverage should you aim for?](https://www.atlassian.com/continuous-delivery/software-testing/code-coverage#:~:text=There%27s%20no%20silver%20bullet%20in%20code%20coverage%2C%20and,coverage%20is%20a%20good%20goal%20to%20aim%20for.)

There's no silver bullet in code coverage, and a high percentage of coverage
could still be problematic if critical parts of the application are not being
tested, or if the existing tests are not robust enough to properly capture
failures upfront. With that being said it is **generally accepted that 80% coverage
is a good goal to aim for**. Trying to reach a higher coverage might turn out to
be costly, while not necessary producing enough benefit.