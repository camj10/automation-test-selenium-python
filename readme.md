# 🧪 Selenium and Python Practices

This repository contains practices developed with **Selenium and Python**, focused on web test automation, covering topics from basic concepts to advanced techniques.

## 📚 Contents

1. **First Test with Selenium**
   - Installation of Selenium and Pytest.
   - Creation and execution of a basic test.

2. **WebElements**
   - Identification and manipulation of web elements.
   - Use of locators: ID, Name, XPath, CSS Selectors.

3. **Actions**
   - Advanced interactions: clicks, double clicks, drag and drop.
   - Handling keyboard and mouse events.

4. **Browser Configurations**
   - Customizing browser options.
   - Running in headless mode and managing profiles.

5. **Design Patterns**
   - Introduction to testing-related design patterns.
   - Best practices for structuring test code.

6. **Page Object Model (POM)**
   - Implementation of the POM pattern.
   - Separation of test logic and page representation.

7. **BDD (Behavior Driven Development)**
   - Using tools like Behave.
   - Writing scenarios in natural language.

8. **Allure Reports**
   - Generating detailed and visual reports.
   - Integration with Pytest for automated report generation.

9. **`pytest.ini` Configuration**
   - Customizing test execution.
   - Defining default options and markers.

## 🛠️ Project Requirements

- Python 3.8 or higher
- Selenium
- Pytest
- Allure
- Behave *(optional, for BDD)*

Install dependencies:

```bash
pip install -r requirements.txt



🧪  Running Tests
To run tests with pytest:

```bash
pytest

To generate the report with Allure:

```bash
pytest --alluredir=reports/allure
allure serve reports/allure
