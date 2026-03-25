# initialize project
init:
	uv init

# updates packages
install:
	uv sync

# starts the application
app:
	uv run streamlit run main.py
