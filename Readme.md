# MLOPS Course

This repository contains code for a project that includes a simple function, a FastAPI app, and Dockerization. The project aims to demonstrate the following steps:

1. **Create a Simple Function**: The repository includes a script with a simple function. This function performs a specific task.

2. **Add Test Case for the Simple Function**: A test case is added to verify the correctness and expected behavior of the simple function. This ensures that the function performs as intended.

3. **Add requirements.txt File**: A requirements.txt file is included in the repository to specify the dependencies required by the project. These dependencies can be installed easily using the file.

4. **Create Makefile**: A Makefile is provided with several functions to streamline common tasks during development. The Makefile supports the following functions:
   - `install`: Installs the project dependencies specified in the requirements.txt file.
   - `lint`: Runs a linter to check the code for any potential issues or inconsistencies.
   - `test`: Executes the test cases to validate the functionality of the code.

5. **Add GitHub Action**: A GitHub Action workflow is implemented to automate the linting and testing processes. This ensures that the code is consistently checked for quality and functionality.

6. **Create a FastAPI App**: A FastAPI application is created with at least two endpoints. One endpoint supports the GET method, while the other supports the POST method. These endpoints handle specific requests and provide appropriate responses.

7. **Add Test Cases for FastAPI App's Endpoints**: Test cases are added to validate the functionality of the FastAPI app's endpoints. These test cases ensure that the endpoints respond correctly to various requests.

8. **Add Logging to the App**: Logging functionality is implemented within the FastAPI app to capture relevant information during its execution. This aids in troubleshooting and monitoring the application.

9. **Create Dockerfile**: A Dockerfile is included in the repository to define the necessary steps to build a Docker image of the project.

10. **Build Docker Image**: Using the Dockerfile, a Docker image is built that encapsulates the project and its dependencies. This allows for consistent deployment and execution across different environments.

11. **Push Image to the Repository**: The built Docker image is pushed to the repository, making it available for deployment and distribution.

Feel free to explore the repository and leverage the provided functionalities for your own projects or learning purposes.

