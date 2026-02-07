# Home Assistant Integration Template - Complete Reference Guide

**Version:** 1.0.0
**Date:** February 7, 2026
**Template Version:** Python 3.14.2 | Home Assistant 2026.2.0

This comprehensive guide documents the complete setup and usage of this Home Assistant integration development template, including AI agents, automation, and best practices.

---

## Table of Contents

1. [Overview](#overview)
2. [Project Structure](#project-structure)
3. [AI Agent System](#ai-agent-system)
4. [Automation Infrastructure](#automation-infrastructure)
5. [Development Workflows](#development-workflows)
6. [Quality Standards](#quality-standards)
7. [Quick Reference](#quick-reference)
8. [Troubleshooting](#troubleshooting)

---

## Overview

### What This Template Provides

This is a production-ready template for developing Home Assistant custom integrations with:

- ✅ **Complete Development Environment** - Python 3.14.2, HA 2026.2.0, all tools
- ✅ **AI Agent Assistance** - Specialized agents for Claude Code, Copilot, Codex
- ✅ **Automated Quality Enforcement** - CI/CD, pre-commit hooks, VS Code tasks
- ✅ **Testing Framework** - pytest with HA custom component support
- ✅ **Code Quality Tools** - Ruff, mypy, pre-commit
- ✅ **Example Integration** - Working template following best practices
- ✅ **Comprehensive Documentation** - Guides, patterns, troubleshooting

### Key Features

| Feature | Description | Status |
|---------|-------------|--------|
| **Python Environment** | Virtual environment with Python 3.14.2 | ✅ Ready |
| **Home Assistant** | HA Core 2026.2.0 installed | ✅ Ready |
| **Testing** | pytest + pytest-homeassistant-custom-component | ✅ Ready |
| **Linting** | Ruff (official HA standard) | ✅ Ready |
| **Type Checking** | mypy with strict mode | ✅ Ready |
| **Pre-commit** | Git hooks for quality gates | ✅ Ready |
| **CI/CD** | GitHub Actions pipeline | ✅ Ready |
| **AI Agents** | Claude, Copilot, Codex integration | ✅ Ready |
| **VS Code Tasks** | Interactive development tasks | ✅ Ready |
| **Makefile** | Command-line interface | ✅ Ready |
| **Documentation** | Complete guides and examples | ✅ Ready |

---

## Project Structure

### Directory Layout

```
ha-template/
├── .github/                              # GitHub configuration
│   ├── workflows/
│   │   └── ci.yml                        # CI/CD pipeline
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml                # Bug report form
│   │   ├── feature_request.yml           # Feature request form
│   │   └── config.yml                    # Template config
│   ├── pull_request_template.md          # PR checklist
│   ├── dependabot.yml                    # Dependency updates
│   ├── copilot-instructions.md           # GitHub Copilot context
│   └── AUTOMATION_GUIDE.md               # Automation documentation
│
├── .vscode/                              # VS Code configuration
│   ├── settings.json                     # Editor settings
│   ├── tasks.json                        # Development tasks
│   └── codex-instructions.md             # Codex context
│
├── custom_components/                    # HA integrations
│   └── example_integration/              # Example template
│       ├── __init__.py                   # Integration entry point
│       ├── manifest.json                 # Integration metadata
│       ├── config_flow.py                # Config flow (UI setup)
│       ├── const.py                      # Constants
│       ├── strings.json                  # UI strings
│       └── translations/
│           └── en.json                   # English translations
│
├── tests/                                # Test suite
│   ├── conftest.py                       # Shared fixtures
│   └── README.md                         # Testing guide
│
├── scripts/                              # Utility scripts
│   └── verify_environment.py             # Environment verification
│
├── resources/                            # Development resources
│   └── agents/
│       └── ha-integration-agent/         # HA development agent
│           ├── README.md                 # Installation & usage guide
│           ├── ha_integration_agent_system_prompt.md  # Agent definition
│           ├── ha_integration_agent_spec.md           # Comprehensive patterns
│           └── [example files]           # Reference implementations
│
├── venv/                                 # Virtual environment (gitignored)
│
├── CLAUDE.md                             # Project instructions for Claude
├── README.md                             # Project overview
├── SETUP_COMPLETE.md                     # Setup summary
├── REFERENCE_GUIDE.md                    # This file
├── ha-dev-environment-requirements.md    # Environment setup guide
├── Makefile                              # Command-line interface
├── pyproject.toml                        # Project configuration
├── .pre-commit-config.yaml               # Pre-commit hooks
└── .gitignore                            # Git ignore rules
```

### Key Files Explained

#### Configuration Files

| File | Purpose | When to Edit |
|------|---------|--------------|
| `pyproject.toml` | Ruff, mypy, pytest config | Rarely - already optimized |
| `.pre-commit-config.yaml` | Git hook configuration | When adding new hooks |
| `.vscode/settings.json` | VS Code editor settings | Personal preference |
| `CLAUDE.md` | Instructions for Claude Code | When patterns change |

#### Documentation Files

| File | Purpose | Audience |
|------|---------|----------|
| `README.md` | Project overview | All developers |
| `CLAUDE.md` | Claude Code instructions | AI assistant |
| `SETUP_COMPLETE.md` | Setup summary | Initial setup |
| `REFERENCE_GUIDE.md` | Complete reference (this file) | All developers |
| `ha-dev-environment-requirements.md` | Environment setup | Setup phase |
| `.github/AUTOMATION_GUIDE.md` | Automation details | Maintainers |

#### Automation Files

| File | Purpose | Tool |
|------|---------|------|
| `.github/workflows/ci.yml` | CI/CD pipeline | GitHub Actions |
| `.vscode/tasks.json` | Interactive tasks | VS Code |
| `Makefile` | CLI commands | Make |
| `.pre-commit-config.yaml` | Git hooks | Pre-commit |
| `.github/dependabot.yml` | Dependency updates | Dependabot |

---

## AI Agent System

### Overview

This template includes specialized AI agents to assist with Home Assistant integration development.

### Installed Agents

#### 1. HA Integration Agent (Claude Code)

**Location:** `~/.claude/agents/ha-integration-agent.md`

**Capabilities:**
- Generates complete integration structure
- Creates DataUpdateCoordinator implementations
- Builds config flows with all steps
- Generates entity platform files
- Writes test files with proper mocking
- Reviews code against Quality Scale
- Provides architecture guidance

**How to Use:**

```python
# Method 1: Task tool
Task(
    subagent_type="ha-integration-agent",
    prompt="Help me create a config flow for OAuth2 authentication",
    description="Create OAuth2 config flow"
)

# Method 2: Chat interface
@agent ha-integration-agent
I need to create an integration for [device/service]...
```

**When to Use:**
- Starting a new integration (architecture planning)
- Implementing patterns (DataUpdateCoordinator, config flow)
- Code review (Quality Scale compliance)
- Debugging (understanding errors)
- Learning (understanding WHY patterns exist)

#### 2. GitHub Copilot Integration

**Location:** `.github/copilot-instructions.md`

**Auto-Detection:** GitHub Copilot automatically reads this file

**What It Does:**
- Suggests DataUpdateCoordinator patterns
- Generates async-first code
- Creates proper config flows
- Follows HA type hint conventions
- Implements error handling
- Creates unique IDs for entities

**How to Use:**
```python
# Just start typing, Copilot suggests HA-compliant code
class SmartThermostatCoordinator(DataUpdateCoordinator):
    # Press Tab - Copilot suggests implementation
```

#### 3. VS Code Codex Integration

**Location:** `.vscode/codex-instructions.md`

**How to Use:**
```python
# Add comment referencing pattern
# Generate DataUpdateCoordinator following HA Quality Scale Bronze tier
class MyCoordinator(DataUpdateCoordinator):
    # Codex generates based on context
```

### Agent Documentation

#### Complete Installation Guide
**File:** `resources/agents/ha-integration-agent/README.md` (655 lines)

**Contents:**
- Installation instructions for all 3 platforms
- Usage examples with code
- Agent capabilities reference
- Code patterns (DataUpdateCoordinator, Config Flow, Entities)
- Quality Scale requirements
- Common pitfalls
- Testing requirements
- Troubleshooting
- Best practices

#### Comprehensive Specification
**File:** `resources/agents/ha-integration-agent/ha_integration_agent_spec.md` (750 lines)

**Contents:**
- Executive summary
- Core knowledge base (Python versions, Quality Scale)
- Critical development patterns
- Complete manifest.json reference
- Testing requirements
- Common pitfalls and solutions
- Development environment setup
- Agent workflow phases
- Community resources

#### Agent System Prompt
**File:** `resources/agents/ha-integration-agent/ha_integration_agent_system_prompt.md` (190 lines)

**Contents:**
- Agent core identity
- Structured workflow (Discovery → Implementation → Quality)
- Technical requirements enforcement
- Communication style guidelines
- Common Q&A

---

## Automation Infrastructure

### Four Automation Layers

This template provides **four complementary automation systems**:

```
┌─────────────────────────────────────────┐
│ 1. GitHub Actions (CI/CD)              │
│    Runs on: push, PR                    │
│    Enforces: Bronze tier minimum        │
└─────────────────────────────────────────┘
                    ↑
┌─────────────────────────────────────────┐
│ 2. Pre-commit Hooks                     │
│    Runs on: git commit                  │
│    Catches: Style, type, format issues  │
└─────────────────────────────────────────┘
                    ↑
┌─────────────────────────────────────────┐
│ 3. VS Code Tasks                        │
│    Runs on: Ctrl+Shift+B (manual)       │
│    Provides: Interactive feedback       │
└─────────────────────────────────────────┘
                    ↑
┌─────────────────────────────────────────┐
│ 4. Makefile Commands                    │
│    Runs on: make <command> (manual)     │
│    Provides: CLI interface              │
└─────────────────────────────────────────┘
```

### 1. GitHub Actions CI/CD

**File:** `.github/workflows/ci.yml`

**Triggers:**
- Push to `main` or `testing` branches
- Pull requests to `main` or `testing`
- Manual workflow dispatch

**Jobs:**

| Job | Command | Duration | Required |
|-----|---------|----------|----------|
| **Lint** | `ruff check` + `ruff format --check` | ~30s | ✅ |
| **Type Check** | `mypy custom_components/` | ~45s | ✅ |
| **Test** | `pytest tests/` (Python 3.13 & 3.14) | ~2min | ✅ |
| **Verify Env** | `python scripts/verify_environment.py` | ~1min | ✅ |
| **All Checks** | Gate job (all must pass) | ~1s | ✅ |

**Features:**
- Matrix testing (Python 3.13 and 3.14)
- Pip dependency caching
- Coverage report generation
- Codecov upload (optional)
- Detailed error reporting

**Setup Codecov (Optional):**
1. Sign up: https://codecov.io/
2. Add repository
3. Get token
4. Add GitHub secret: `CODECOV_TOKEN`

### 2. VS Code Tasks

**File:** `.vscode/tasks.json`

**Quick Access:** Press `Ctrl+Shift+B` (Linux/Windows) or `Cmd+Shift+B` (Mac)

**Available Tasks:**

| Task | Shortcut | Description |
|------|----------|-------------|
| **Quality Check (All)** | `Ctrl+Shift+B` | Default: lint, format, type-check, test |
| Run All Tests | Task menu | pytest tests/ -v |
| Run Tests with Coverage | Task menu | pytest with HTML report |
| Lint with Ruff | Task menu | Check code for issues |
| Lint and Fix with Ruff | Task menu | Auto-fix linting issues |
| Format with Ruff | Task menu | Format code |
| Type Check with mypy | Task menu | Check type hints |
| Run Pre-commit Hooks | Task menu | Run all hooks |
| Verify Environment | Task menu | Verify setup |
| Open Coverage Report | Task menu | Open htmlcov/index.html |

**How to Use:**
1. Press `Ctrl+Shift+P` → "Tasks: Run Task"
2. Or press `Ctrl+Shift+B` for default build
3. Or Terminal menu → "Run Task..."

**Problem Matchers:**
- Ruff errors show inline
- mypy errors show inline
- pytest failures show in Problems panel

### 3. Makefile Commands

**File:** `Makefile`

**View All Commands:** `make help`

**Quick Reference:**

```bash
# Setup
make setup             # Complete project setup
make install           # Install dependencies
make verify            # Verify environment

# Quality Checks
make quality           # All checks (lint, format, type, test)
make lint              # Lint only (check)
make lint-fix          # Lint with auto-fix
make format            # Format code
make type-check        # Type check
make pre-commit        # Run pre-commit hooks

# Testing
make test              # Run all tests
make test-cov          # Tests with HTML coverage
make test-specific FILE=path  # Run specific test
make watch-test        # Auto-run tests on changes

# Development
make new-integration NAME=x   # Create new integration
make list-integrations        # List integrations
make coverage-report          # Open coverage HTML
make ci                       # Simulate CI locally
make clean                    # Remove build artifacts
make info                     # Show project info
```

**Colored Output:**
- 🔵 Blue: Informational messages
- 🟢 Green: Success messages
- 🟡 Yellow: Warnings
- 🔴 Red: Errors

**Examples:**

```bash
# Create new integration
make new-integration NAME=smart_thermostat
# Output: custom_components/smart_thermostat/ created

# Run all quality checks
make quality
# Runs: lint-fix → format → type-check → test

# Simulate CI before pushing
make ci
# Runs exact CI checks locally

# Development mode with auto-tests
make watch-test
# Requires: sudo apt install entr
```

### 4. Pre-commit Hooks

**File:** `.pre-commit-config.yaml`

**Runs Automatically:** On every `git commit`

**Installed Hooks:**

| Hook | Purpose | Auto-Fix |
|------|---------|----------|
| trailing-whitespace | Remove trailing spaces | ✅ |
| end-of-file-fixer | Ensure newline at EOF | ✅ |
| check-yaml | Validate YAML syntax | ❌ |
| check-added-large-files | Prevent files >500KB | ❌ |
| check-merge-conflict | Detect conflict markers | ❌ |
| ruff | Lint Python code | ✅ |
| ruff-format | Format Python code | ✅ |
| mypy | Type check Python code | ❌ |

**Manual Execution:**

```bash
# Run on all files
pre-commit run --all-files

# Run on specific files
pre-commit run --files custom_components/my_integration/*.py

# Run specific hook
pre-commit run ruff --all-files

# Update hook versions
pre-commit autoupdate

# Reinstall hooks
pre-commit clean
pre-commit install
```

**Skip Hooks (Emergency Only):**
```bash
# NOT RECOMMENDED
git commit --no-verify -m "Emergency fix"

# Better: Fix the issues
pre-commit run --all-files
git add .
git commit -m "Fixed issues"
```

### 5. Dependabot

**File:** `.github/dependabot.yml`

**Schedule:** Weekly on Mondays at 9:00 AM

**Monitors:**
- Python packages (pip)
- GitHub Actions versions

**Dependency Groups:**

| Group | Packages |
|-------|----------|
| **Home Assistant** | homeassistant, aiohttp, voluptuous |
| **Testing** | pytest, pytest-asyncio, pytest-homeassistant-custom-component, pytest-cov |
| **Code Quality** | ruff, mypy, pre-commit |

**Configuration:**
- Max 10 open PRs for pip
- Max 5 open PRs for GitHub Actions
- Auto-labels: `dependencies`, `python`, `github-actions`
- Commit prefix: `deps:` or `ci:`

**⚠️ Action Required:**
Edit `.github/dependabot.yml` and replace `your-github-username` with your actual GitHub username in the `reviewers` and `assignees` fields.

### 6. Issue & PR Templates

#### Bug Report Template
**File:** `.github/ISSUE_TEMPLATE/bug_report.yml`

**Collects:**
- Bug description
- Steps to reproduce
- Expected behavior
- Log output
- HA version, integration version, Python version
- Configuration (sanitized)
- Additional context

#### Feature Request Template
**File:** `.github/ISSUE_TEMPLATE/feature_request.yml`

**Collects:**
- Problem description
- Proposed solution
- Alternatives considered
- Affected entity platforms
- Willingness to contribute
- Additional context

#### PR Template
**File:** `.github/pull_request_template.md`

**Sections:**
- Description & issue reference
- Type of change
- Quality tier target
- Testing verification
- Comprehensive checklist (27 items)
- Screenshots/logs
- Additional notes

**Checklist Categories:**
- Code Quality
- Testing
- Async Requirements
- DataUpdateCoordinator
- Entities
- Config Flow
- Documentation
- Pre-commit Hooks

---

## Development Workflows

### Initial Setup

```bash
# 1. Activate virtual environment
cd /home/chris/projects/ha-template
source venv/bin/activate

# 2. Verify environment
make verify
# or: python scripts/verify_environment.py

# Expected: ✓ All checks passed!

# 3. Install pre-commit hooks (if not already done)
pre-commit install
```

### Creating a New Integration

#### Method 1: Using Makefile (Recommended)

```bash
make new-integration NAME=smart_thermostat
```

**Output:**
```
Creating new integration: smart_thermostat...
Integration created: custom_components/smart_thermostat
Next steps:
  1. Update custom_components/smart_thermostat/manifest.json
  2. Update custom_components/smart_thermostat/const.py (DOMAIN)
  3. Implement your integration logic
  4. Run 'make quality' to check your code
```

#### Method 2: Manual Copy

```bash
cp -r custom_components/example_integration custom_components/smart_thermostat
```

#### Step-by-Step Implementation

1. **Update manifest.json:**
   ```json
   {
     "domain": "smart_thermostat",
     "name": "Smart Thermostat",
     "version": "1.0.0",
     "codeowners": ["@your-username"],
     "config_flow": true,
     "documentation": "https://github.com/...",
     "integration_type": "device",
     "iot_class": "local_polling",
     "requirements": ["your-api-library==1.0.0"]
   }
   ```

2. **Update const.py:**
   ```python
   DOMAIN: Final = "smart_thermostat"
   DEFAULT_SCAN_INTERVAL: Final = 30
   ```

3. **Implement coordinator.py:**
   - Create DataUpdateCoordinator subclass
   - Implement `_async_update_data()`
   - Handle errors properly

4. **Create config_flow.py:**
   - Implement user step
   - Add error handling
   - Create strings.json

5. **Implement entity platforms:**
   - sensor.py, climate.py, etc.
   - Extend base entity class
   - Use CoordinatorEntity pattern

6. **Write tests:**
   ```bash
   touch tests/test_smart_thermostat_config_flow.py
   touch tests/test_smart_thermostat_init.py
   ```

7. **Run quality checks:**
   ```bash
   make quality
   ```

### Development Cycle

#### Standard Workflow

```bash
# 1. Edit code
# Edit custom_components/your_integration/...

# 2. Run quality checks
make quality
# or: Ctrl+Shift+B in VS Code

# 3. Fix any issues
make lint-fix
make format

# 4. Run tests
make test

# 5. Check coverage
make test-cov
make coverage-report

# 6. Commit (pre-commit hooks run automatically)
git add .
git commit -m "Add feature X"

# 7. Push (CI runs automatically)
git push
```

#### Watch Mode (Development)

```bash
# Auto-run tests on file changes
make watch-test

# In another terminal, edit code
# Tests run automatically when you save
```

### Testing Workflows

#### Run All Tests

```bash
# Option 1: Makefile
make test

# Option 2: Direct
pytest tests/ -v

# Option 3: VS Code Task
# Ctrl+Shift+P → Tasks: Run Task → Run All Tests
```

#### Run with Coverage

```bash
# Generate HTML report
make test-cov

# Open in browser
make coverage-report

# Or manually
pytest tests/ --cov=custom_components --cov-report=html
xdg-open htmlcov/index.html
```

#### Run Specific Tests

```bash
# Using Make
make test-specific FILE=tests/test_config_flow.py

# Direct
pytest tests/test_config_flow.py -v

# Specific test function
pytest tests/test_config_flow.py::test_user_flow -v
```

### Testing Best Practices

#### ✅ DO: Module-Level Imports

Import integration code at the module level, not inside test functions:

```python
# ✅ CORRECT - Module level
from custom_components.your_integration import PLATFORMS, async_setup_entry

async def test_setup():
    assert async_setup_entry is not None

# ❌ WRONG - Inside function
async def test_setup():
    from custom_components.your_integration import async_setup_entry  # Don't!
    assert async_setup_entry is not None
```

**Why:** Pytest imports test modules during collection, before fixtures run. Module-level imports work correctly, but imports inside functions can fail with path resolution issues.

#### ✅ DO: Clear Caches When Type Checking Fails

```bash
# Mypy giving weird errors? Clear cache!
rm -rf .mypy_cache
mypy custom_components/

# Pre-commit mypy acting different? Rebuild environment
pre-commit clean
pre-commit install
```

**Why:** Mypy caches type information for performance. Stale caches cause confusing, inconsistent errors.

#### ✅ DO: Test Both Ways

```bash
# Test with manual commands
mypy custom_components/
pytest tests/ -v

# Test with pre-commit (what CI uses)
pre-commit run --all-files

# Test with full CI simulation
make ci
```

**Why:** Pre-commit and CI run in isolated environments that can behave differently than your local setup.

#### ✅ DO: Ensure Package Structure

```bash
# Required files for proper Python imports
custom_components/__init__.py              # Makes it a package
custom_components/your_integration/        # Your integration
tests/conftest.py                          # Adds path to sys.path
```

**Why:** Without `__init__.py`, Python won't treat custom_components as a package, causing import errors.

#### ❌ DON'T: Override Tool Configs in Pre-commit

```yaml
# ❌ BAD - Overrides mypy.ini
- id: mypy
  args: [--strict, --ignore-missing-imports]

# ✅ GOOD - Uses mypy.ini
- id: mypy
  additional_dependencies:
    - homeassistant
```

**Why:** Command-line args override config files, causing inconsistent behavior between manual runs and pre-commit.

### Quality Check Workflows

#### Before Committing

```bash
# Run all quality checks
make quality

# Or individual checks
make lint-fix      # Auto-fix linting
make format        # Format code
make type-check    # Check types
make test          # Run tests
```

#### Before Creating PR

```bash
# Simulate CI locally
make ci

# Should output:
# [1/4] Linting...
# ✓ Linting passed
# [2/4] Format check...
# ✓ Format check passed
# [3/4] Type checking...
# ✓ Type check passed
# [4/4] Tests...
# ✓ All tests passed
# All CI checks passed! ✓
```

#### Continuous Checks (VS Code)

```bash
# Set up format-on-save
# .vscode/settings.json already configured

# Run checks manually
# Ctrl+Shift+B → Quality Check (All)
```

### Git Workflow

#### Standard Flow

```bash
# 1. Create feature branch
git checkout -b feature/new-sensor

# 2. Make changes
# ... edit files ...

# 3. Run quality checks
make quality

# 4. Commit (hooks run automatically)
git add .
git commit -m "Add new sensor platform"

# 5. Push
git push origin feature/new-sensor

# 6. Create PR on GitHub
# CI runs automatically
```

#### Pre-commit Hooks

Hooks run automatically on commit:
- Remove trailing whitespace
- Fix end-of-file
- Validate YAML
- Lint with Ruff
- Format with Ruff
- Type check with mypy

**If hooks fail:**
```bash
# Hooks auto-fix what they can
# Review changes
git add .

# Commit again
git commit -m "Add new sensor platform"
```

---

## Quality Standards

### Integration Quality Scale

#### Bronze Tier (Minimum Required)

**Requirements:**
- ✅ Config flow UI setup
- ✅ Automated setup tests
- ✅ Basic coding standards (Ruff passes)
- ✅ Proper manifest.json

**How to Achieve:**
```bash
# Must pass these checks
make lint          # Ruff must pass
make test          # Basic tests must pass
make type-check    # No critical type errors
```

**Example:**
```python
# Config flow required
class MyConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1
    # Implementation...

# Tests required
async def test_form(hass):
    result = await hass.config_entries.flow.async_init(DOMAIN, ...)
    assert result["type"] == "form"
```

#### Silver Tier (Reliability)

**Requirements:**
- ✅ All Bronze requirements
- ✅ Proper error handling (auth failures, offline devices)
- ✅ Entity availability management
- ✅ Troubleshooting documentation
- ✅ Log-once patterns for connection issues

**How to Achieve:**
```python
# Proper error handling in coordinator
async def _async_update_data(self):
    try:
        return await self.client.async_get_data()
    except AuthenticationError as err:
        raise ConfigEntryAuthFailed from err  # Triggers reauth
    except ConnectionError as err:
        raise UpdateFailed(f"Error: {err}") from err  # Marks unavailable

# Availability handling in entities
@property
def available(self) -> bool:
    return super().available and self._device_id in self.coordinator.data
```

#### Gold Tier (Feature Complete)

**Requirements:**
- ✅ All Silver requirements
- ✅ Full async codebase (no blocking operations)
- ✅ Comprehensive test coverage (>80%)
- ✅ Complete type annotations (mypy strict passes)
- ✅ Efficient data handling

**How to Achieve:**
```bash
# Must pass these checks
make type-check    # mypy must pass with 0 errors
make test-cov      # Coverage >80%

# All I/O must be async
# Use aiohttp, not requests
# Use async libraries for all operations
```

#### Platinum Tier (Excellence)

**Requirements:**
- ✅ All Gold requirements
- ✅ All coding standards and best practices
- ✅ Clear code comments and documentation
- ✅ Optimal performance
- ✅ Active code ownership and maintenance

**How to Achieve:**
- Document all complex logic
- Optimize performance (minimal API calls)
- Respond to issues promptly
- Keep dependencies updated

### Mandatory Patterns

#### 1. DataUpdateCoordinator (REQUIRED for Polling)

```python
from datetime import timedelta
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)
from homeassistant.exceptions import ConfigEntryAuthFailed

class MyCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    """Coordinator to manage data fetching."""

    def __init__(self, hass: HomeAssistant, client: MyApiClient) -> None:
        """Initialize coordinator."""
        super().__init__(
            hass,
            logger=_LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=30),
            always_update=False,  # False if data implements __eq__
        )
        self.client = client

    async def _async_update_data(self) -> dict[str, Any]:
        """Fetch data from API."""
        try:
            return await self.client.async_get_data()
        except AuthenticationError as err:
            raise ConfigEntryAuthFailed("Invalid credentials") from err
        except ConnectionError as err:
            raise UpdateFailed(f"Connection error: {err}") from err
```

**Why:** Centralizes data fetching, prevents duplicate polls, handles errors properly, manages entity availability.

#### 2. Config Flow (REQUIRED for All New Integrations)

```python
from homeassistant import config_entries
from homeassistant.data_entry_flow import FlowResult
import voluptuous as vol

class MyConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle config flow."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle user step."""
        errors: dict[str, str] = {}

        if user_input is not None:
            try:
                info = await self._async_validate_input(user_input)
            except CannotConnect:
                errors["base"] = "cannot_connect"
            except InvalidAuth:
                errors["base"] = "invalid_auth"
            else:
                await self.async_set_unique_id(info["unique_id"])
                self._abort_if_unique_id_configured()
                return self.async_create_entry(
                    title=info["title"],
                    data=user_input,
                )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({...}),
            errors=errors,
        )
```

**Why:** Provides consistent UI experience, required for Bronze tier, mandatory for core integrations.

#### 3. Async-First Architecture (REQUIRED)

```python
# ✅ CORRECT - Async library
import aiohttp

async def fetch_data(self, url: str) -> dict[str, Any]:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

# ❌ WRONG - Blocks event loop
import requests

async def fetch_data(self, url: str) -> dict[str, Any]:
    return requests.get(url).json()  # BLOCKS ENTIRE HA!

# ✅ ACCEPTABLE - If no async library exists
async def fetch_data(self, url: str) -> dict[str, Any]:
    return await self.hass.async_add_executor_job(
        requests.get, url
    )
```

**Why:** Home Assistant is async. Blocking operations freeze the entire system.

#### 4. Full Type Hints (REQUIRED)

```python
from __future__ import annotations

from typing import Any, Final

# ✅ CORRECT - Modern syntax
DOMAIN: Final = "my_integration"
DEFAULT_TIMEOUT: Final[int] = 30

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
) -> bool:
    """Set up from config entry."""
    data: dict[str, Any] = entry.data
    devices: list[str] = data.get("devices", [])

# ❌ WRONG - Old syntax
from typing import List, Dict

devices: List[str] = []  # Use list[str]
data: Dict[str, Any] = {}  # Use dict[str, Any]
```

**Why:** Type safety, IDE support, Gold tier requirement, modern Python standard.

#### 5. CoordinatorEntity Pattern (REQUIRED)

```python
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.helpers.device_registry import DeviceInfo

class MyEntity(CoordinatorEntity[MyCoordinator]):
    """Base entity."""

    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: MyCoordinator,
        device_id: str,
    ) -> None:
        """Initialize entity."""
        super().__init__(coordinator)
        self._device_id = device_id

    @property
    def device_info(self) -> DeviceInfo:
        """Return device info."""
        return DeviceInfo(
            identifiers={(DOMAIN, self._device_id)},
            name=self.coordinator.data[self._device_id]["name"],
        )

    @property
    def unique_id(self) -> str:
        """Return unique ID."""
        return f"{DOMAIN}_{self._device_id}_{self._entity_type}"

    @property
    def available(self) -> bool:
        """Return availability."""
        return (
            super().available
            and self._device_id in self.coordinator.data
        )
```

**Why:** Automatic updates, proper availability handling, device grouping, unique IDs.

### Anti-Patterns (What NOT to Do)

#### ❌ Blocking the Event Loop

```python
# WRONG
data = requests.get(url).json()  # Blocks entire HA

# CORRECT
async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
        data = await response.json()
```

#### ❌ Manual Polling in __init__.py

```python
# WRONG
async def async_setup_entry(hass, entry):
    async def update():
        # Fetch and update...
    async_track_time_interval(hass, update, 30)

# CORRECT
async def async_setup_entry(hass, entry):
    coordinator = MyCoordinator(hass, client)
    await coordinator.async_config_entry_first_refresh()
```

#### ❌ Missing Unique IDs

```python
# WRONG
@property
def unique_id(self) -> str:
    return self._name  # Name can change!

# CORRECT
@property
def unique_id(self) -> str:
    return f"{DOMAIN}_{self._device_id}_{self._sensor_type}"
```

#### ❌ Not Handling Unavailability

```python
# WRONG
class MySensor(SensorEntity):
    pass  # No availability check

# CORRECT
class MySensor(CoordinatorEntity):
    @property
    def available(self) -> bool:
        return super().available and self._device_id in self.coordinator.data
```

#### ❌ YAML Configuration

```python
# WRONG - Don't do this for new integrations
async def async_setup_platform(hass, config, async_add_entities):
    # NO! Use config flow instead
```

---

## Quick Reference

### Essential Commands

```bash
# Environment
source venv/bin/activate              # Always first!
make verify                           # Check setup

# Development
make quality                          # All checks
make test                             # Run tests
make test-cov                         # Tests + coverage
make ci                               # Simulate CI

# Git
git add .                             # Stage changes
git commit -m "message"               # Commit (hooks run)
git push                              # Push (CI runs)

# Create Integration
make new-integration NAME=device_name
```

### Keyboard Shortcuts (VS Code)

| Shortcut | Action |
|----------|--------|
| `Ctrl+Shift+B` | Run default build task (Quality Check All) |
| `Ctrl+Shift+P` | Command palette → "Tasks: Run Task" |
| `Ctrl+`\` | Toggle terminal |
| `Ctrl+Shift+M` | Show problems panel |

### File Locations Cheat Sheet

```bash
# Agent files
~/.claude/agents/ha-integration-agent.md           # Claude agent
.github/copilot-instructions.md                     # Copilot context
.vscode/codex-instructions.md                       # Codex context

# Documentation
CLAUDE.md                                           # Claude instructions
README.md                                           # Project overview
REFERENCE_GUIDE.md                                  # This file
resources/agents/ha-integration-agent/README.md     # Agent guide

# Automation
.github/workflows/ci.yml                            # CI/CD pipeline
.vscode/tasks.json                                  # VS Code tasks
Makefile                                            # CLI commands
.pre-commit-config.yaml                             # Git hooks

# Configuration
pyproject.toml                                      # Tool config
.vscode/settings.json                               # Editor settings
```

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Import errors | `source venv/bin/activate` |
| Tests failing | `make clean && make install && make test` |
| Linting errors | `make lint-fix && make format` |
| Type errors | `mypy custom_components/your_integration/` |
| CI failing locally passing | `make ci` to simulate exact CI |
| Pre-commit failing | `pre-commit run --all-files` |

### Quality Checklist

Before committing:
- [ ] `make quality` passes
- [ ] No TODO/FIXME comments
- [ ] Tests added for new functionality
- [ ] Type hints on all functions
- [ ] Docstrings on public API

Before creating PR:
- [ ] `make ci` passes
- [ ] Coverage hasn't decreased
- [ ] PR template filled out
- [ ] Breaking changes documented

---

## Troubleshooting

### Environment Issues

#### Problem: Import Errors

```bash
# Symptom
ModuleNotFoundError: No module named 'homeassistant'

# Solution
source venv/bin/activate
make verify
```

#### Problem: Tools Not Found

```bash
# Symptom
bash: ruff: command not found

# Solution
source venv/bin/activate
which ruff  # Should show path in venv/
```

#### Problem: Virtual Environment Missing

```bash
# Solution
python3.14 -m venv venv
source venv/bin/activate
make install
make verify
```

### Testing Issues

#### Problem: Tests Can't Import custom_components

**Symptoms:**
```bash
ModuleNotFoundError: No module named 'custom_components'
ModuleNotFoundError: No module named 'custom_components.your_integration'
```

**Root Causes:**
1. Missing `custom_components/__init__.py` - Python doesn't treat it as a package
2. Project root not in Python path during tests
3. Imports placed inside test functions instead of module level

**Solution:**
```bash
# 1. Ensure __init__.py exists
touch custom_components/__init__.py

# 2. Verify conftest.py setup
cat tests/conftest.py
# Should contain:
#   import sys
#   from pathlib import Path
#   custom_components_path = Path(__file__).parent.parent / "custom_components"
#   sys.path.insert(0, str(custom_components_path.parent))

# 3. Use module-level imports in tests
# CORRECT:
from custom_components.your_integration import PLATFORMS

async def test_platforms():
    assert PLATFORMS is not None

# INCORRECT:
async def test_platforms():
    from custom_components.your_integration import PLATFORMS  # Don't import here!
    assert PLATFORMS is not None

# 4. Run tests
source venv/bin/activate
pytest tests/ -v
```

**Why:** Pytest imports test modules during collection phase, before fixtures run. Module-level imports work correctly, but imports inside test functions execute after fixture setup, which can cause path resolution issues.

#### Problem: Mypy Type Check Failures

**Symptoms:**
```bash
error: Cannot find implementation or library stub for module named "homeassistant.config_entries"
error: Returning Any from function declared to return "bool"
KeyError: 'setter_type'  # Cache corruption
```

**Root Causes:**
1. Home Assistant type stubs not found by mypy
2. Corrupted mypy cache
3. Pre-commit mypy config differs from mypy.ini

**Solution:**
```bash
# 1. Clear mypy cache (fixes most issues)
rm -rf .mypy_cache

# 2. Verify mypy.ini configuration
cat mypy.ini
# Should contain:
#   [mypy-homeassistant]
#   ignore_missing_imports = True
#
#   [mypy-homeassistant.*]
#   ignore_missing_imports = True

# 3. Update pre-commit config
# In .pre-commit-config.yaml, ensure:
#   - repo: https://github.com/pre-commit/mirrors-mypy
#     hooks:
#       - id: mypy
#         additional_dependencies:
#           - homeassistant  # Must be here!
#           - types-requests

# 4. Rebuild pre-commit environment
pre-commit clean
pre-commit install

# 5. Test both ways
mypy custom_components/              # Direct mypy
pre-commit run mypy --all-files      # Pre-commit mypy
```

**Why:** Mypy caches type information for performance. Stale caches cause confusing errors. Pre-commit runs mypy in an isolated environment that needs homeassistant installed separately.

#### Problem: Coverage Decreased

```bash
# Check what's not covered
make test-cov
make coverage-report

# Add tests for red lines
# Commit and rerun
```

### Automation Issues

#### Problem: CI Passing Locally But Failing on GitHub

```bash
# Solution: Simulate exact CI environment
make ci

# If still passes locally, check:
# - Python version match (3.13 vs 3.14)
# - Clean environment
make clean
rm -rf venv/
python3.13 -m venv venv
source venv/bin/activate
make install
make ci
```

#### Problem: Pre-commit Hooks Not Running

```bash
# Solution
pre-commit install
pre-commit run --all-files
```

#### Problem: Pre-commit Hooks Failing

```bash
# Auto-fix what's possible
pre-commit run --all-files

# If still failing, check specific hook
pre-commit run ruff --all-files
pre-commit run mypy --all-files

# Fix issues manually, then commit
```

### Git Issues

#### Problem: Large Files in Commit

```bash
# Symptom
Error: File ... is 5.00 MB; this is larger than GitHub's maximum file size

# Solution
# Check .gitignore includes:
venv/
__pycache__/
*.pyc
.coverage
htmlcov/
.pytest_cache/
.mypy_cache/
.ruff_cache/

# Remove from git
git rm --cached path/to/large/file
git commit -m "Remove large file"
```

#### Problem: Merge Conflicts

```bash
# Don't force push or reset unless you understand implications

# Solution
git status
# Edit conflicted files manually
# Remove conflict markers (<<<<, ====, >>>>)
git add .
git commit -m "Resolve merge conflicts"
```

### Agent Issues

#### Problem: Agent Not Responding (Claude Code)

```bash
# Verify installation
ls -lh ~/.claude/agents/ha-integration-agent.md

# Reinstall if missing
cp resources/agents/ha-integration-agent/ha_integration_agent_system_prompt.md \
   ~/.claude/agents/ha-integration-agent.md

# Use explicit invocation
Task(subagent_type="ha-integration-agent", prompt="your question")
```

#### Problem: Copilot Not Using Context

```bash
# Verify file exists
ls -lh .github/copilot-instructions.md

# Keep agent files open in tabs
code resources/agents/ha-integration-agent/ha_integration_agent_spec.md

# Use descriptive comments
# Create DataUpdateCoordinator following HA Bronze tier requirements
```

### Performance Issues

#### Problem: Slow Tests

```bash
# Run specific tests only
pytest tests/test_specific.py -v

# Use parallel execution (if available)
pytest tests/ -n auto

# Skip slow tests during development
pytest tests/ -m "not slow"
```

#### Problem: Slow CI

- Caching is enabled in `.github/workflows/ci.yml`
- If still slow, check matrix (currently Python 3.13 & 3.14)
- Consider reducing matrix for draft PRs

---

## Additional Resources

### Official Documentation

- [Home Assistant Developer Docs](https://developers.home-assistant.io/)
- [Integration Quality Scale](https://developers.home-assistant.io/docs/core/integration-quality-scale/)
- [Creating Your First Integration](https://developers.home-assistant.io/docs/creating_component_index/)

### Community Resources

- [HA Community Forums - Development](https://community.home-assistant.io/c/development/10)
- [HA Discord - Development Channel](https://discord.gg/home-assistant)

### Template Documentation

| Document | Purpose |
|----------|---------|
| [README.md](README.md) | Project overview and quick start |
| [CLAUDE.md](CLAUDE.md) | Instructions for Claude Code |
| [SETUP_COMPLETE.md](SETUP_COMPLETE.md) | Setup summary and verification |
| [ha-dev-environment-requirements.md](ha-dev-environment-requirements.md) | Complete environment setup guide |
| [.github/AUTOMATION_GUIDE.md](.github/AUTOMATION_GUIDE.md) | Detailed automation documentation |
| [resources/agents/.../README.md](resources/agents/ha-integration-agent/README.md) | Agent installation and usage |
| [resources/agents/.../...spec.md](resources/agents/ha-integration-agent/ha_integration_agent_spec.md) | Comprehensive patterns and examples |

### Getting Help

1. **Check documentation first**
   - This guide
   - Agent README
   - Official HA docs

2. **Use the agent**
   ```
   @agent ha-integration-agent
   I'm having trouble with [specific issue]
   ```

3. **Run verification**
   ```bash
   make verify
   make ci
   ```

4. **Check logs**
   - CI logs on GitHub
   - Local test output
   - Home Assistant logs

5. **Community support**
   - HA Community Forums
   - HA Discord
   - GitHub Issues

---

## Version History

| Date | Version | Changes |
|------|---------|---------|
| 2026-02-07 | 1.0.0 | Initial reference guide created |
| 2026-02-07 | 1.0.0 | Added AI agent system documentation |
| 2026-02-07 | 1.0.0 | Added complete automation infrastructure |
| 2026-02-07 | 1.0.0 | Added development workflows and troubleshooting |

---

## Summary

This Home Assistant integration template provides:

✅ **Complete Development Environment**
- Python 3.14.2 + Home Assistant 2026.2.0
- All tools configured and verified

✅ **AI Agent Assistance**
- Claude Code agent installed
- GitHub Copilot integration
- VS Code Codex integration

✅ **Four-Layer Automation**
- GitHub Actions CI/CD
- Pre-commit Git hooks
- VS Code interactive tasks
- Makefile CLI interface

✅ **Quality Enforcement**
- Bronze tier minimum enforced
- Automatic linting & formatting
- Type checking with mypy
- Test coverage tracking

✅ **Complete Documentation**
- Agent guides (655 lines)
- Comprehensive spec (750 lines)
- Automation guide (detailed)
- This reference guide

✅ **Best Practices Built-In**
- DataUpdateCoordinator pattern
- Config flow requirement
- Async-first architecture
- Full type hints
- Proper error handling

**You're ready to build production-quality Home Assistant integrations!** 🚀

---

**Quick Start:**
```bash
source venv/bin/activate
make verify
make new-integration NAME=my_device
make quality
```

**Need Help?** See [Troubleshooting](#troubleshooting) or ask the agent:
```
@agent ha-integration-agent
Help me get started with [your task]
```

---

*Last Updated: February 7, 2026*
*Template Version: 1.0.0*
*Home Assistant Version: 2026.2.0*
