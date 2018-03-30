from wordcloud import WordCloud
import matplotlib.pyplot as plt

def plot_wordcloud(df, column, gender=None):
    if gender is None:
        text = ', '.join([t for t in df[column] if isinstance(t, str)])
        title = column.capitalize() + ' (All Genders)'
    else:
        text = ', '.join([t for t in df[df.gender==gender][column] if isinstance(t, str)])
        title = column.capitalize() + f' ({gender})'
        
    wordcloud = WordCloud(max_font_size=25).generate(text)

    plt.imshow(wordcloud, interpolation="bilinear")
    plt.title(title, fontsize=30)
    plt.axis("off")
    
def plot_all_and_genders_wordcloud(df, column):
    figure = plt.figure(figsize=(16, 18))

    plt.subplot2grid((2, 2), (0, 0), colspan=2)
    plot_wordcloud(loan_data, column)

    plt.subplot2grid((2, 2), (1, 0))
    plot_wordcloud(loan_data, column, gender='male')

    plt.subplot2grid((2, 2), (1, 1))
    plot_wordcloud(loan_data, column, gender='female')
    plt.show()

def draw_wordcloud(df):
    for column in ['tags', 'activity', 'use']:
        plot_all_and_genders_wordcloud(loan_data, column)