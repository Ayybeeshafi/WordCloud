
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import stop_words as sw
import numpy as np
from PIL import Image


def wordcloud(text,stopwordss):
    # Set figure size
    my_mask = np.array(Image.open('angel.png'))
    wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='black', colormap='rainbow', collocations=False, stopwords=stopwordss,mask=my_mask).generate(text)
    # Display image
    plt.figure(figsize=(40, 30))
    plt.axis("off")
    #plt.imshow(wordcloud)
    wordcloud.to_file("wordcloud1.png")


if __name__ == '__main__':


    stop_words = sw.get_stop_words('german')
    print(stop_words)
    file = open("Angelaa.txt")
    line =file.read()
    words = line.split()
    for r in words:
        if not r in stop_words:
            appendFile = open('filteredtext.txt', 'a')
            appendFile.write(" " + r)
            appendFile.close()
    with open('filteredtext.txt', 'r') as txt_file:
        filteredtext = txt_file.read()

    wordcloud(filteredtext,stop_words)