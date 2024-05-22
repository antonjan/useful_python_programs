import matplotlib.pyplot as plt
from wordcloud import Wordcloud
text= 'I love Python Coding because Python is easy to learn and simple'
wordcloud = WordCloud(width=800, height=400).generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Tree')
plt.show()
#clcoding.com
