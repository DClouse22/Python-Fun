# CLAUDE.md

This file provides guidance for AI assistants working with this repository.

## Project Overview

**Python-Fun** is a collection of small, standalone Python projects for learning and entertainment. Each file is an independent script demonstrating different Python capabilities.

## Repository Structure

```
Python-Fun/
├── main.py                    # 3D voxel visualization using matplotlib
├── ChristmasCountdown.py      # Streamlit countdown timer web app
├── Rock Paper Scissors.py     # Streamlit Rock Paper Scissors game
└── CLAUDE.md                  # This file
```

## Project Descriptions

### main.py
A 3D voxel plot visualization using matplotlib. Creates a 5x5x5 colored cube with different colors for each layer (red, green, blue, yellow, white).

**Dependencies:** `matplotlib`, `numpy`

**Run:** `python main.py`

### ChristmasCountdown.py
A Streamlit web application that provides a customizable countdown timer. Users can select a target date and time, then watch the countdown with a progress bar.

**Dependencies:** `streamlit`

**Run:** `streamlit run ChristmasCountdown.py`

### Rock Paper Scissors.py
An interactive Streamlit web game implementing Rock Paper Scissors against the computer. Features score tracking using Streamlit session state.

**Dependencies:** `streamlit`

**Run:** `streamlit run "Rock Paper Scissors.py"`

## Dependencies

The projects use the following Python libraries:
- `matplotlib` - For 3D plotting and visualization
- `numpy` - For numerical array operations
- `streamlit` - For interactive web applications

Install all dependencies:
```bash
pip install matplotlib numpy streamlit
```

## Development Guidelines

### File Naming
- Use descriptive names that indicate the script's purpose
- Spaces in filenames are acceptable (wrap in quotes when running)

### Code Style
- Scripts are standalone and self-contained
- Each script includes all necessary imports at the top
- Use comments to explain non-obvious logic
- Follow PEP 8 conventions

### Adding New Projects
1. Create a new `.py` file with a descriptive name
2. Include all required imports at the top
3. Add `plt.show()` for matplotlib visualizations to display the plot
4. For Streamlit apps, use `st.title()` for the main heading

### Common Fixes Applied
- **matplotlib plots:** Always include `plt.show()` at the end to display visualizations
- **numpy deprecations:** Use `dtype=bool` instead of deprecated `np.bool`

## Git Workflow

- Commit messages should be descriptive of the changes made
- Each script addition/modification should be its own commit
- Pull requests are used for code review on fixes

## Testing

Scripts can be tested by running them directly:
```bash
# For matplotlib scripts
python main.py

# For Streamlit apps
streamlit run ChristmasCountdown.py
streamlit run "Rock Paper Scissors.py"
```

Verify that:
- Matplotlib plots display correctly with proper colors
- Streamlit apps launch without errors and UI elements are interactive
