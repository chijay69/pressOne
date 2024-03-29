# PressOne

# Age Guesser

Age Guesser is a Django web application that guesses the age of a person based on their name using the Agify API.

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/pressOne.git
    ```

2. Navigate to the project directory:
    ```
    cd age-guesser
    ```

3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Apply database migrations:
    ```
    python manage.py migrate
    ```

## Usage

1. Start the Django development server:
    ```
    python manage.py runserver
    ```

2. Open a web browser and go to `http://127.0.0.1:8000/` to access the application.

3. Use a POST request to the following URL to guess the age:
    ```
    POST /get-human-age/
    ```

4. Include the name in the request body as a form parameter or JSON payload:
    ```json
    {
        "name": "John"
    }
    ```

5. Send the POST request to get the guessed age and date of birth.

## Testing

Run the test suite to ensure everything is working correctly:

