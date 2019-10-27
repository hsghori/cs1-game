# Test Plan (Version 1.0.0)

## Professor CS

## 1 Testing Strategy

### 1.1 Overall strategy

For Professor CS, unit and integration testing will be conducted. The team will follow the Test-Driven Development methodology to ensure that tests are effective and functional. However, some tests may be written after due to the fast nature of the development process. After major feature development, we will write integration tests to verify the large scale success of new features with regards to the application as a whole.

### 1.2 Test Selection

1. Unit Testing - All major components should correspond to at least one unit test. Each method within the classes should correspond to a minimum of one unit test. Test-driven development is highly encouraged by developers and should be utilized as much as possible.
    * The concept of the Test-Driven-Development, or TDD, strategy involves the process by which tests are written alongside each function/application component. First the code is written to purposefully fail the test to prove effectiveness of said test. Then, the code is updated to pass the test to confirm accuracy of the code.
    * Some unit tests will be written to inject mock data to test the behavior of the application. One such example would be to insert mock data like a database would, and have the API retrieve it.
1. Integration Testing
    * Integration will be done to test the integration between the components and to tests parts of the interface. Since we have multiple components working together, it is important to implement integration tests to test pieces that unit tests will not cover.

### 1.3 Methods of Testing

1. White Box Testing- Unit testing
    - The testers will use the Statement Coverage Approach to cover a feasible amount of code in a fast prototyping environment.
    - We will be testing ORM models, API views, among other main application features.
  
1. Black Box Testing (Integration Tests)
    - For the integration testst, testers will use the Category Partition method. Tests cases will be selected from a generated list of unique test combinations and written to validate the success of the application.

### 1.4 Adequacy Criterion

We will use the path coverage metric to evaluate the adequacy of our testing suite. Given the overall complexity of our application, 100\% path coverage is not a reasonable goal, but we can aim to achieve 90\% path coverage while developing 
the MVP. 

### 1.5 Bug Tracking
 
The team will use Github's issues tool to track feature progress and debugging. This is both effective and convenient as the team is also using Github for version control of Professor CS's source code.

- Github issues will be tagged based on the type of work that needs to be done- "New Feature", "Task", or "Bug".

- Each issue will have sufficient content explaining steps to reproduce and issue or the steps to complete a task or feature.

- Merge requests will tag the issue number for reference.


### 1.6 Technology

1. Mocha- Mocha is a simple and flexible testing framework that is used to test Javascript componenets.
2. Pytest- The pytest framework is made for writing pythong unit tests. The django.test package will be used for testing the ORM and API layers.
3. Selenium will be used for the integration testing.
2. Testers will use an Integrated development environment (IDE) to develop, run and debug their test


## 2 Test Cases

Test cases and their results will be documented here.
