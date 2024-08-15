# Functional API Test

This project involves setting up a functional test against a web API.

## Test Case

**URL:** [https://www.kurtosys.com](https://www.kurtosys.com)

The following assertions are included in the test case:
- **Status Code:** Ensure that the response status received is `200`.
- **Response Time:** Ensure that the response time is less than 2 seconds.
- **Server Header:** Ensure that the `Server` header has a value of `Cloudflare`.

## How to Run

1. Open your terminal.
2. Ensure the project directory is correctly shown and that the environment is activated.
3. Navigate to the project directory.
4. Run the following command to execute the tests and generate an HTML report:

   ```bash
   pytest --html=report.html --self-contained-html
