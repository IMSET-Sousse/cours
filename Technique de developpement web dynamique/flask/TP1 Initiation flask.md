# TP1 Initiation flask.md

## Steps to Run the Project

1. Install `pipenv` to manage the virtual environment and dependencies:

    ```bash
    pip install pipenv
    ```

2. Install the required packages using `pipenv`:

    ```bash
    python -m pipenv install flask
    ```

3. Create a file named `app.py` and add the following code:

    ```python
    from flask import Flask
    app = Flask(__name__)
    @app.route('/')
    def hello_world():
        return 'Hello, World!'
    if __name__ == '__main__':
        app.run(debug=True)
    ```

4. Run the Flask application:

    ```bash
    pipenv run python app.py
    ```
