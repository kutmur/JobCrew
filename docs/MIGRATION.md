# Migration Guide: v0.x to v1.0

## Overview

JobCrew v1.0 introduces a standardized project structure that follows Python packaging best practices. This guide will help you migrate from the old flat structure to the new organized structure.

## What Changed?

### Old Structure (v0.x)
```
JobCrew/
├── agents.py
├── tasks.py
├── main.py
├── tools/
│   └── search_tools.py
├── requirements.txt
├── .env.example
└── README.md
```

### New Structure (v1.0)
```
JobCrew/
├── src/
│   └── jobcrew/           # Main application package
│       ├── agents.py
│       ├── tasks.py
│       ├── main.py
│       └── tools/
│           └── search_tools.py
├── config/
│   └── .env.example
├── docs/
│   └── AGENTS.md
├── run.py                 # New entry point
├── pyproject.toml         # New package configuration
└── requirements.txt
```

## Migration Steps

### 1. Pull the Latest Changes

```bash
git pull origin main
```

### 2. Reinstall Dependencies

The package can now be installed in development mode:

```bash
# Recommended: Install as editable package
pip install -e .

# Alternative: Install from requirements.txt
pip install -r requirements.txt
```

### 3. Update Your .env File

The `.env.example` file has moved to `config/.env.example`. However, your `.env` file should still remain in the project root.

If you don't have a `.env` file yet:
```bash
cp config/.env.example .env
# Then edit .env with your API keys
```

### 4. Update How You Run the Application

**Old way (v0.x):**
```bash
python main.py
```

**New ways (v1.0):**
```bash
# Option 1: Using the entry point (if installed with pip install -e .)
jobcrew

# Option 2: Using the run script
python run.py

# Option 3: Direct module execution
python -m jobcrew.main
```

### 5. Update Custom Code (If Applicable)

If you've customized the code and import from JobCrew modules, update your imports:

**Old imports:**
```python
from agents import JobAgents
from tasks import JobTasks
from tools.search_tools import job_search_tool
```

**New imports:**
```python
from jobcrew.agents import JobAgents
from jobcrew.tasks import JobTasks
from jobcrew.tools.search_tools import job_search_tool
```

## Benefits of the New Structure

1. **Professional Package Structure**: Follows Python packaging best practices
2. **Easier Installation**: Can be installed with `pip install -e .`
3. **Better Organization**: Logical separation of source code, config, and docs
4. **Namespace Protection**: All code is under the `jobcrew` package namespace
5. **Cleaner Root Directory**: Less clutter, easier to navigate
6. **Command Line Entry Point**: Can run with `jobcrew` command after installation

## Backward Compatibility

The old files (`agents.py`, `tasks.py`, `main.py`, `tools/`) are marked as deprecated and will be removed in a future version. They are currently ignored by git (see `.gitignore`).

## Troubleshooting

### Import Errors

If you get import errors like `ModuleNotFoundError: No module named 'jobcrew'`:

1. Make sure you've installed the package:
   ```bash
   pip install -e .
   ```

2. Verify the installation:
   ```bash
   python -c "import jobcrew; print('Success!')"
   ```

### Old Files Still Present

The old files at the root level are now deprecated. They are listed in `.gitignore` and won't be tracked by git. You can safely delete them:

```bash
rm agents.py tasks.py main.py
rm -rf tools/
```

However, if you have local modifications, make sure to port them to the new structure first.

### Environment Variables Not Found

Make sure your `.env` file is in the project root (not in the `config/` directory). The `config/` directory only contains the template.

```bash
# Verify .env location
ls -la .env

# If missing, create from template
cp config/.env.example .env
# Then add your API keys
```

## Need Help?

If you encounter any issues during migration:

1. Check the updated [README.md](../README.md) for current usage instructions
2. Review the [AGENTS.md](AGENTS.md) for detailed agent documentation
3. Open an issue on GitHub if problems persist

## Summary

The migration is straightforward:
1. ✅ Pull latest changes
2. ✅ Reinstall with `pip install -e .`
3. ✅ Use `python run.py` or `jobcrew` to run
4. ✅ Update imports if you have custom code
5. ✅ Enjoy the improved structure!
