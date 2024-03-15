from flask import Flask, render_template, request
import spacy
import dill,joblib,gzip,pickle,mgzip



app = Flask(__name__)

#Load spacy pipeline
nlp  = spacy.load('en_core_web_lg')

#Load recommender function
with open('recomend_movie.pickle','rb') as f:
    recommend_movie = dill.load(f)
    f.close()



# Sample movie descriptions and titles
movie_descriptions = {
    "The Shawshank Redemption": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
    "The Godfather": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
    "The Dark Knight": "When the menace known as The Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.",
    # Add more movie descriptions here
}

print(recommend_movie("When the menace known as The Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham."))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend_movie_desc():
    input_description = request.form["description"].strip()
    top_recommendations = recommend_movie(input_description)
    print(top_recommendations)
    
        
    return render_template("recommendations.html", recommendations=top_recommendations)

if __name__ == "__main__":
    
    app.run(debug=True)
