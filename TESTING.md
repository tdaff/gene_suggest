# Testing

## What strategies would you employ to test your application?

Testing is currently implemented using the ``pytest`` framework. The testing
can be seen at https://travis-ci.org/tdaff/gene_suggest where the software
is tested against two versions of python. Some forms of testing that are
currently employed or should be considered in future are:

- Unit testing. Test the output of individual functions for a variety of inputs
  Tests should cover all edge cases and failure cases. Some simple tests have
  been added for the functions in the interface module.
- Regression testing. Test the outputs of the application as a whole. These
  have been implemented as request calls to the flask application. Could also
  be tested as a script that makes cURL calls. Ensure that the results
  never change from known good results.
- Testing against a mock database. Rather than testing against the live
  database, it would be better and faster to test against a static database,
  with fixed, know outputs.
- UI testing. A framework like Selenium can be used to test how the application
  works in a browser with user interaction for user facing web components.
- Stress testing. Test the performance of the application under heavy load.

New versions of software may also be deployed to staging servers before going
fully live for real-world testing with the ability to roll back to a known
good configuration at any time.

## How would you automate testing?

Automatic testing is already implemented using Travis CI which runs the test
suite with two versions of Python and will alert the developers when an error
is encountered. Many other automated testing frameworks are available, such as
Jenkins locally or integrated into online code hosting like Bitbucket or
GitLab. These usually require a file that describes the build environment,
how to install the code and then how to run the tests. They may also be used
to deploy the application for a successful build.