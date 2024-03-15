# Movie Recommendation App

The Movie Recommendation App is a simple web application built with Flask and SpaCy that recommends similar movies based on user input descriptions. Users can input a brief description of a movie they like, and the app will provide a list of recommended movies with similar descriptions.

## Features

- **Simple Interface**: Users can easily input a movie description through a text area and submit it to get recommendations.
- **Text Similarity**: Utilizes SpaCy's natural language processing capabilities to calculate the similarity between movie descriptions.
- **Responsive Design**: The application's UI is designed to be responsive and accessible across different devices.

## Setup

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/your-username/movie-recommendation-app.git
    ```

2. **Install Dependencies**:

    Navigate into the project directory:

    ```bash
    cd movie-recommendation-app
    ```

    Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. **Download SpaCy Language Model**:

    Download the SpaCy English language model:

    ```bash
    python -m spacy download en_core_web_md
    ```

4. **Run the Application**:

    Start the Flask server:

    ```bash
    python app.py
    ```

5. **Access the Application**:

    Open your web browser and go to `http://localhost:5000`.

## Usage

1. **Input Description**: Enter a brief description of a movie you like in the provided text area.
2. **Get Recommendations**: Click on the "Get Recommendations" button to receive a list of recommended movies with similar descriptions.
3. **Explore Recommendations**: Explore the recommended movies and discover new titles to watch.

## Technologies Used

- **Flask**: Python web framework used for building the backend server.
- **HTML/CSS**: Frontend styling and layout.
- **SpaCy**: Python library for natural language processing used to analyze and compare movie descriptions.
- **Sci-kit Learn**: Python library for Machine learning used for preprocessing.
- **Pandas**: Python library for loading and manipulating the datasets 
- **Git**: Version control system for tracking changes to the codebase.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please fork the repository, make your changes, and submit a pull request.

Please ensure that your code follows PEP 8 guidelines and includes appropriate documentation where necessary.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
