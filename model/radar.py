# -*- coding: utf-8 -*- #
import numpy as np
import matplotlib.pyplot as plt
from gensim.models import KeyedVectors

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('ggplot')

vectors_path = '../data/vectors.txt'

brand_name = [u'吸金']
key_words = [u'詐騙', u'投資', u'賠償', u'金額', u'犯罪']


def caculate_cosine_similarity():
    model = KeyedVectors.load_word2vec_format(vectors_path, binary=False)
    result = []
    for word in key_words:
        result.append(model.similarity(brand_name, word)[0])
    print(result)
    return result


def draw_radar():
    angles = np.linspace(0, 2*np.pi, len(key_words), endpoint=False)
    angles = np.concatenate((angles, [angles[0]]))

    cs = caculate_cosine_similarity()
    cs = np.concatenate((cs, [cs[0]]))

    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)

    ax.plot(angles, cs, 'o-', lw=1, label=brand_name)
    ax.fill(angles, cs, alpha=0.25)
    ax.set_thetagrids(angles*180/np.pi, key_words)
    ax.set_ylim(0, 1.1)
    ax.set_theta_zero_location('N')
    plt.legend(loc=1)
    ax.grid(True)
    plt.show()


# caculate_cosine_similarity()
draw_radar()
