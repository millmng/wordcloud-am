# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 15:32:56 2018

@author: milli

Generating a square wordcloud from text extracted from PDF version of the holy bible in Amharic
"""

import pdfParser as pp
import matplotlib.pyplot as plt
from wordcloud import WordCloud
plt.figure(figsize=(15,10))

#
the_bible_url = 'http://bible.geezexperience.com/amharic/download/AmharicBible.pdf'
text = pp.parse_pdf(the_bible_url)

#removing stop words
stop_words = open('data\stopwords.txt', encoding='utf-8').read().split()
filtered_text_list = [val for val in text if val not in stop_words]
filtered_text = ' '.join(filtered_text_list)

wordcloud = WordCloud(font_path='fonts\jiretsl.ttf',
                      relative_scaling = 0.8,
                      min_font_size=4,
                      background_color="white",
                      width=744,
                      height=400,
                      scale=3,
                      font_step=1,
                      collocations=False,
                      margin=2
                      ).generate(filtered_text)

plt.imshow(wordcloud, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()
plt.savefig('examples\\the_bible2.png',dpi=600)