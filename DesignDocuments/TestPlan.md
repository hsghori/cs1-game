# Test Plan (Version 1.0.0)

## Professor CS

## 1 Testing Strategy

### 1.1 Overall strategy

Our overall testing strategy is to develop unit tests in parallel with feature development to catch bugs before they 
are merged into the master branch. After major feature development we will write integration tests to verify the large 
scale success of new features with regards to the application as a whole.

### 1.2 Test Selection

We will mainly rely on white box testing to create unit tests for individual application components (ORM models, 
API views, etc) and run black box tests to validate the success 
of the application. 

### 1.3 Adequacy Criterion

We will use the path coverage metric to evaluate the adequacy of our testing suite. Given the overall complexity of our 
application, 100\% path coverage is not a reasonable goal, but we can aim to achieve 90\% path coverage while developing 
the MVP. 

### 1.4 Bug Tracking

We will use Github issues to track bug reports and feature requests. 
 
### 1.5 Technology

We will use python's `pytest` framework for python unit tests specifically using the `django.test` package for 
testing the ORM and API layer. We will use `Mocha`, `Jest`, `Enzyme`, and `Sinon` for javascript testing. We 
will use `selenium` for integration testing. 

## 2 Test Cases


