import spacy 
nlp = spacy.load('en_core_web_md')

hulk_movie = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the\
illuminati trick Hulk into a shuttle and launch him into space to a planet where Hulk can live in peace.\
 Unfortunately, Hulk lands on the planet Sakar where he is sold into slavery and trained as a gladiator."

movie_list = []
with open('movies.txt', "r") as userfile:
    for line in userfile:
        movie_list.append(line)

print("-------------Movie similarity---------------")
for token in movie_list:
    token = nlp(token)
    for token_ in movie_list:
        token_ = nlp(token_)

similarity_values = []
similarity_values.append(token)

model_sentence = nlp(hulk_movie)
closest_movie = 0
movie_details = ""
for sentence in movie_list:
    doc = nlp(sentence)
    similiarity = doc.similarity(model_sentence)
    print(sentence + " - ", similiarity)
    if similiarity > closest_movie:
        closest_movie = similiarity
        movie_details = "The closest movie is " + sentence + " - ", similiarity 
print(movie_details)

