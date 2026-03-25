## How to run the project locally
### Cloning the project
To clone the project first make sure **git** is installed on your system, then, run the following command:
```bash
git clone https://github.com/bngno/streamlit_csv_converter.git
```
### Prepping evironment
#### Starting virtual enviroment (run once)
In the project's directory prepare the environment to run the application with:
```bash
make init # initializes project
make install # synchronize dependencies
``` 
> [!IMPORTANT]
> To use the given commands, the **uv** ([repo](https://github.com/astral-sh/uv)) project manager needs to be installed at first.
### Running the project
#### Starting the application
Start the application with:
```bash
make app
```