# 🚀 Mastering PyTest – Beginner to Advanced Guide

A comprehensive, step-by-step learning repository to master Python testing with PyTest. From basics to production-grade automation frameworks.

---

## 📋 Quick Navigation

| Topic                   | Details                                                |
| ----------------------- | ------------------------------------------------------ |
| **Best For**      | Beginners, QA Engineers, Test Automation Professionals |
| **Level**         | Beginner → Advanced                                   |
| **Duration**      | 4-8 weeks                                              |
| **Prerequisites** | Python 3.12+, Basic Python knowledge                   |

---

## 🎯 What You'll Learn

- ✅ PyTest fundamentals and best practices
- ✅ Write reusable fixtures and conftest configurations
- ✅ Organize production-style automation frameworks
- ✅ Generate professional reports (HTML & Allure)
- ✅ Execute tests in parallel for speed
- ✅ Set up CI/CD with GitHub Actions
- ✅ Ace PyTest automation interviews

---

## ✨ Key Features

- **Beginner-Friendly Examples** – Clear, practical code
- **Production-Style Structure** – Industry-standard folder layout
- **Step-by-Step Approach** – Learn progressively
- **Reusable Components** – Fixtures, fixtures scopes, conftest
- **Advanced Topics** – Markers, parameterization, parallel execution
- **Professional Reports** – HTML & Allure dashboards
- **CI/CD Ready** – GitHub Actions included
- **Interview Prep** – Common questions & answers

---

## 🛠 Tech Stack

```
Python 3.12+          → Programming Language
PyTest                → Testing Framework
Requests              → API Testing
pytest-html           → HTML Reports
Allure                → Advanced Reporting
pytest-xdist          → Parallel Execution
GitHub Actions        → CI/CD Pipeline
```

---

## 📦 Prerequisites & Setup

### 1️⃣ Install Python

```bash
python --version  # Requires 3.12+
```

### 2️⃣ Clone Repository

```bash
git clone https://github.com/<your-username>/mastering-pytest.git
cd mastering-pytest
```

### 3️⃣ Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Verify Installation

```bash
pytest --version          # Should show pytest 8.x.x
python -m pytest --version
```

---

## 📂 Project Structure

```
mastering-pytest/
├── .github/
│   └── workflows/
│       └── pytest.yml                 # GitHub Actions CI/CD
├── tests/
│   ├── conftest.py                   # Shared fixtures & config
│   ├── test_assertions.py            # Assertion examples
│   ├── test_classes.py               # Test class patterns
│   ├── test_fixtures.py              # Fixture usage
│   ├── test_fixture_scope.py         # Fixture scopes
│   ├── test_parameterize.py          # Parameterization
│   ├── test_markers.py               # Markers (@pytest.mark)
│   ├── test_skip.py                  # Skip/XFail
│   ├── test_parallel.py              # Parallel execution
│   └── test_allure_demo.py           # Allure reporting
├── utilities/                         # Reusable helpers
├── test_data/                        # External test data
├── reports/                          # Generated HTML reports
├── allure-results/                   # Allure raw results
├── allure-report/                    # Allure final report
├── pytest.ini                        # PyTest configuration
├── requirements.txt                  # Dependencies
├── README.md                         # Documentation
└── .gitignore                        # Git ignore rules
```

---

## 📚 Learning Path

### Phase 1: Fundamentals (Week 1)

- [ ] Test functions & naming conventions
- [ ] Test classes & organization
- [ ] Assertions & exception handling
- [ ] Test discovery & execution

### Phase 2: Core Features (Week 2-3)

- [ ] Fixtures & setup/teardown
- [ ] Fixture scopes (function, class, session)
- [ ] conftest.py configuration
- [ ] Parameterization & markers

### Phase 3: Advanced Topics (Week 4)

- [ ] Yield fixtures
- [ ] Skip & XFail
- [ ] Parallel execution with pytest-xdist
- [ ] Custom markers

### Phase 4: Reporting & CI/CD (Week 5-6)

- [ ] HTML reports
- [ ] Allure reporting
- [ ] GitHub Actions setup
- [ ] Test data management

### Phase 5: Interview Prep (Week 7-8)

- [ ] Common PyTest questions
- [ ] Framework design patterns
- [ ] Best practices
- [ ] Troubleshooting

---

## 🚀 Common Commands

### Run Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Show print statements
pytest -s

# Run specific file
pytest tests/test_assertions.py

# Run specific test
pytest tests/test_assertions.py::test_addition

# Run specific class
pytest tests/test_classes.py::TestCalculator
```

### Advanced Execution

```bash
# Stop after first failure
pytest -x

# Stop after N failures
pytest --maxfail=2

# Run by marker
pytest -m smoke

# Run by keyword
pytest -k login

# Parallel execution (8 workers)
pytest -n auto
```

### Reporting

```bash
# Generate HTML report
pytest --html=reports/report.html

# Generate Allure results
pytest --alluredir=allure-results

# Generate & open Allure report
allure serve allure-results
```

---

## 📊 Dependencies

```txt
pytest>=8.0.0              # Testing framework
pytest-html>=4.0.0         # HTML reporting
pytest-xdist>=3.0.0        # Parallel execution
allure-pytest>=2.13.0      # Allure reporting
requests>=2.31.0           # API testing
```

Install all:

```bash
pip install -r requirements.txt
```

---

## ✅ Setup Checklist

- [ ] Python 3.12+ installed
- [ ] Git installed
- [ ] Repository cloned
- [ ] Virtual environment created & activated
- [ ] Dependencies installed
- [ ] `pytest --version` works
- [ ] First test runs successfully
- [ ] HTML report generated

---

## 🎓 Learning Modules

| Module           | Topics                           | Duration  |
| ---------------- | -------------------------------- | --------- |
| Fundamentals     | Functions, Classes, Assertions   | 3-5 hours |
| Fixtures         | Setup/Teardown, Scopes, conftest | 4-6 hours |
| Markers          | @pytest.mark, Custom markers     | 2-3 hours |
| Parameterization | Multiple test cases from data    | 2-3 hours |
| Reporting        | HTML, Allure, Custom reports     | 3-4 hours |
| Advanced         | Plugins, Hooks, Framework design | 5-8 hours |

---

## 💡 Best Practices

✅ **Naming** – Use clear, descriptive names (`test_user_login_success`)
✅ **Organization** – One feature per file (`test_login.py`, `test_checkout.py`)
✅ **Assertions** – One logical assertion per test
✅ **Fixtures** – Keep fixtures focused and reusable
✅ **Independence** – Tests should not depend on execution order
✅ **Data** – Store test data externally (JSON, CSV)
✅ **Documentation** – Use docstrings for complex tests
✅ **CI/CD** – Always run tests before merging

---

## ⚠️ Common Issues

| Issue                         | Solution                                                  |
| ----------------------------- | --------------------------------------------------------- |
| `ModuleNotFoundError`       | Run`pip install -r requirements.txt`                    |
| `pytest not found`          | Activate virtual environment                              |
| Tests not discovered          | Check file/function names (`test_*.py`, `def test_*`) |
| Allure command not found      | Install Allure CLI separately                             |
| Permission denied (Mac/Linux) | Run`chmod +x venv/bin/activate`                         |

---

## 🏆 Real-World Example

**File:** `tests/test_calculator.py`

```python
import pytest

class TestCalculator:
    """Test suite for calculator operations"""
  
    def test_addition(self):
        assert 2 + 2 == 4
  
    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            10 / 0
  
    @pytest.mark.skip(reason="Not implemented yet")
    def test_square_root(self):
        assert 4 ** 0.5 == 2
```

**Run:**

```bash
pytest tests/test_calculator.py -v
```

---

## 📖 Interview Questions Covered

✓ What is PyTest and why use it?
✓ Difference between unittest and PyTest
✓ How does test discovery work?
✓ What are fixtures and conftest?
✓ Explain fixture scopes
✓ How to parameterize tests?
✓ What are markers and custom markers?
✓ Skip vs XFail
✓ Parallel execution setup
✓ Reporting and CI/CD integration

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Follow PEP 8 style guide
4. Add tests for new features
5. Submit a pull request

---

## 📚 Additional Resources

- [Official PyTest Docs](https://docs.pytest.org/)
- [Allure Documentation](https://docs.qameta.io/allure/)
- [GitHub Actions Guide](https://docs.github.com/en/actions)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

---

## 📄 License

This project is licensed under the MIT License – see LICENSE file for details.

---

## 🎉 Quick Start (30 seconds)

```bash
# 1. Clone
git clone https://github.com/<username>/mastering-pytest.git
cd mastering-pytest

# 2. Setup
python -m venv venv
source venv/bin/activate  # Mac/Linux: or venv\Scripts\activate (Windows)

# 3. Install
pip install -r requirements.txt

# 4. Run
pytest -v

# 5. Report
pytest --html=reports/report.html
```

---

## 💬 Support

- 📖 Check the documentation first
- 🐛 Create an issue for bugs
- 💡 Discuss ideas in discussions
- ❓ FAQ section in the wiki

---

**Happy Testing! 🧪✨**

*Master PyTest. Build Better Tests. Land Your Dream QA Role.*
