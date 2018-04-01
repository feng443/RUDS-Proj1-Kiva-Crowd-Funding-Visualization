from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os

stopwords = set(STOPWORDS)
stopwords.add("user_favorite")

def plot_wordcloud(df, column, gender=None):
    if gender is None:
        text = ', '.join([t for t in df[column] if isinstance(t, str)])
        title = column.capitalize() + ' (All Genders)'
    else:
        text = ', '.join([t for t in df[df.gender==gender][column] if isinstance(t, str)])
        title = column.capitalize() + f' ({gender})'
    
    mask = np.array(
        Image.open(
            os.path.join(
                'resource',
                f'{gender}.png' if gender else 'earth.png')))
    
    wordcloud = WordCloud(
        background_color='white',
        #max_words=200,
        max_font_size=25,
        mask=mask,
        stopwords=stopwords,
    ).generate(text)

    plt.imshow(wordcloud, interpolation="bilinear")
    plt.title(title, fontsize=30)
    plt.axis("off")
    
def plot_all_and_genders_wordcloud(df, column):
    figure = plt.figure(figsize=(16, 10))

    plt.subplot2grid((2, 2), (1, 0))
    plot_wordcloud(df, column, gender='male')

    plt.subplot2grid((2, 2), (1, 1))
    plot_wordcloud(df, column, gender='female')
    plt.savefig(os.path.join('image', f'kiva_data_map_{column}.png'))
    plt.show()

def draw_wordcloud(df):
    for column in ['tags', 'activity', 'use']:
        plot_all_and_genders_wordcloud(df, column)