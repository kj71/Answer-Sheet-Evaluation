# import necessary libraries
import tensorflow_hub as hub
import tensorflow as tf

# Load pre-trained universal sentence encoder model
embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")


def similarity_score(x, y):
    # Sentences for which you want to create embeddings,
    # passed as an array in embed()
    Sentences = [x, y]
    embeddings = embed(Sentences)

    s = tf.keras.losses.cosine_similarity(embeddings[0], embeddings[-1])
    return s