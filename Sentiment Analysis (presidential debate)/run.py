import sys
from collections import defaultdict
from utils import *

pos_threshold = .01
neg_threshold = -.01

def presidential_senti_dist(authors, comments, name_anchors, analyzer):
    assert len(authors) == len(comments)
    sentiments = defaultdict(list)
    author_supports = defaultdict(dict)
    for idx in range(len(comments)):
        polarity = sent_sentiment(comments[idx], analyzer)
        for name, anchors in name_anchors.items():
            if about_who(comments[idx], anchors):
                sentiments[name].append(polarity)
                try:
                    author_supports[authors[idx]][name] += polarity
                except:
                    author_supports[authors[idx]][name] = polarity
    return sentiments, author_supports

def sent_sentiment(sent, analyzer):
    if analyzer == 'textblob':
        from textblob import TextBlob
        testimonial = TextBlob(sent)
        polarity = testimonial.sentiment.polarity
        if polarity > pos_threshold:
            # print 'positive'
            return 1
        elif polarity < neg_threshold:
            # print 'negative'
            return -1
        else:
            # print 'neutral'
            return 0
    elif analyzer == 'vader':
        from vaderSentiment.vaderSentiment import sentiment as vaderSentiment
        try:
            vs = vaderSentiment(sent)
        except:
            vs = vaderSentiment(sent.encode('utf8'))
        if vs['pos'] > vs['neg'] and vs['pos'] > vs['neu']:
            return 1
        elif vs['neg'] > vs['neu']:
            return -1
        else:
            return 0
    else:
        raise ValueError("Got incorrect analyzer type: %s" % analyzer)

if __name__ == '__main__':
    usage = 'python run.py [corpus_path]'
    try:
        corpus_path = sys.argv[1]
    except:
        print usage
    analyzer = 'textblob'
    candidates = {'clinton':['hillary', 'clinton', ' her ', ' she '], 'trump':['donald', 'trump', ' him ', ' he ']}

    corpus = MyCorpus(corpus_path)
    author_id, comments = zip(*corpus)
    print "totally %s comments" % len(comments)
    sentiments, author_supports = presidential_senti_dist(author_id, comments, candidates, analyzer)
    print ", ".join(["%s of them are about %s" % (len(v), k.title()) for k, v in sentiments.items()])

    stats_comments = stats(sentiments)
    print "sentiment (positive (1)/negative (-1)/neutral (0)) distribution"
    print stats_comments

    print "totally %s authors" % len(set(author_id))
    stats_supports = stats_author(author_supports)
    print ", ".join(["%s of them support %s" % (len(v), k.title()) for k, v in stats_supports.items()])

    # save to disk
    save_json(sentiments, 'sentiments.txt')
    save_json(stats_comments, 'stats_comments.txt')
    save_json(stats_supports, 'stats_supports.txt')
