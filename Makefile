# base configurations
VENV := .venv

# commads
# creares the virtual environment (venv)
venv:
	python -m venv $(VENV)

# updating pip and installing and updating dependencies
install:
	pip install --upgrade pip;
	pip install -r requirements.txt;

# starting the application
app: install
	streamlit run main.py

# cleaning the set environment
clean:
	rm -rf $(VENV)