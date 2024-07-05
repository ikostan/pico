# Testing PiPico W Training

[![codecov](https://codecov.io/gh/ikostan/pico/branch/master/graph/badge.svg?token=UV5L6GPUG8)](https://codecov.io/gh/ikostan/pico)

## Static Code Analysis

Static code analysis consists of a series of automated checks performed on source code.
A static analysis tool scans code for common known errors and vulnerabilities,
such as memory leaks or buffer overflows. The analysis can also enforce coding standards.

### Tools:

**1. flake8:** tool for style guide enforcement.

Flake8 is a wrapper around these tools:
- PyFlakes
- pycodestyle
- Ned Batchelder's McCabe script

**2. pylint:** analyses your code without actually running it. It checks for errors,
enforces a coding standard, looks for code smells, and can make suggestions about how
the code could be refactored.

**3. mypy:** is an optional static type checker for Python that aims to combine the
benefits of dynamic (or "duck") typing and static typing. Mypy combines the expressive
power and convenience of Python with a powerful type system and compile-time type checking.

**4. Markdown lint:** A tool to check markdown files and flag style issues.

## Automated Testing
![Test Automation Pyramid](https://github.com/ikostan/pico/blob/master/img/TestAutomationPyramid.png)

Automation testing is ideal for repetitive tasks and produces more consistent results
than the manual process, as people inevitably risk missing details or performing checks
inconsistently when asked to do the same steps over and over again.

### Unit Testing

Unit tests rightly form the basis of the testing pyramid. These tests are designed to
ensure your code works as you expect by addressing the smallest possible unit of behavior.
For teams that have decided to invest in writing unit tests, developers typically take
responsibility for writing them as they write the code.

### Component Testing

As the name suggests, Component testing involves analyzing multiple functions and code
modules before they form software. It is a black box testing technique that evaluates the
application without considering the code information.

### Component Testing vs Unit Testing: Key Differences

While Component testing and Unit testing are done in the different stages of SDLC,
they are closely related, but technically both are different. Here’s a table for you
to easily understand Component testing vs Unit testing:

![Component Testing vs Unit Testing](https://github.com/ikostan/pico/blob/master/img/component_vs_unit.webp)

### Integration Testing

With integration tests, you ensure that multiple parts of your software interact with each
other as expected, such as the interaction between some application code and a database.

### E2E Testing

Also known as full-stack tests, end-to-end tests look at the entire application.
While they can be run through the GUI, they don’t have to be; an API call can also exercise
multiple parts of the system (although APIs can also be checked with integration tests).
The testing pyramid recommends having a smaller number of these tests, not only because they
take longer to run but also because they tend to be brittle.

### System Testing

System Testing is carried out on the whole system in the context of either system requirement
specifications or functional requirement specifications or in contest of both. System testing
tests the design and behavior of the system and also the expectations of the customer. 

### Difference Between System Testing and E2E Testing

System Testing is a type of testing that is performed on the complete system or software
application to evaluate its behavior and performance. It is generally conducted after the
completion of the integration testing phase and is carried out in a production-like environment.
The primary objective of System Testing is to identify defects or bugs that may have been missed
during the earlier phases of testing and ensure that the system meets the specified requirements.

On the other hand, End-to-end Testing is a type of testing that evaluates the entire software
system, including its integration with other systems or external interfaces. It is typically
performed in a simulated production environment and involves testing the software from the user’s
perspective. The objective of End-to-end Testing is to ensure that the software system meets the
customer’s requirements and expectations and that all components work together seamlessly.

### Manual Testing

It is a technique to test the software that is carried out using the functions and features of
an application. In manual software testing, a tester tests the software by following a set of
predefined test cases. In this testing, testers make test cases for the codes, test the software,
and give the final report about that software. Manual testing is time-consuming because it is done
by humans, and there is a chance of human errors.

### Test Environments

Both performance and end-to-end tests require environments that are very similar to
production and may require build test data. For an automated testing regime to provide
confidence in the software under test, it’s important for build tests to be run in the
same way each time, and that includes ensuring test environments remain consistent between
runs (although they should be updated to match production when changes are applied there).

### Code Coverage

Code coverage is a metric that can help you understand how much of your source is tested.
It's a very useful metric that can help you assess the quality of your test suite.

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