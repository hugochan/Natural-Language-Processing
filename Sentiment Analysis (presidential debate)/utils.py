import os
import json
from collections import Counter
from collections import defaultdict

candidates = {'clinton':['hillary', 'clinton'], 'trump':['donald', 'trump']}

class MyCorpus(object):
    """a memory-friendly iterator"""
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            fpath = os.path.join(self.dirname, fname)
            if not os.path.isfile(fpath) or fname[0] == '.':
                continue
            try:
                with open(fpath) as fp:
                    data = json.load(fp)
                    for each in data['items']:
                        line = each['snippet']['topLevelComment']['snippet']
                        yield (line['authorChannelId']['value'], line['textDisplay'].lower())
            except Exception as e:
                raise e
            else:
                fp.close()

def about_who(sent, anchors):
    for each in anchors:
        if each in sent:
            return True
    return False

def stats(sentiments):
    stats_ = {}
    for k, v in sentiments.items():
        total = float(len(v))
        stats_[k] = dict([(x, round(y / total, 3)) for x, y in Counter(v).items()])
    return stats_

def stats_author(author_supports):
    stats_ = defaultdict(list)
    for k, v in author_supports.items():
        if not v:
            continue

        if candidates.keys()[0] in v and candidates.keys()[1] in v:
            if v[candidates.keys()[0]] > v[candidates.keys()[1]]:
                stats_[candidates.keys()[0]].append(k)
            elif v[candidates.keys()[0]] < v[candidates.keys()[1]]:
                stats_[candidates.keys()[1]].append(k)
        elif candidates.keys()[0] in v:
            if v[candidates.keys()[0]] > 0:
                stats_[candidates.keys()[0]].append(k)
            elif v[candidates.keys()[0]] < 0:
                stats_[candidates.keys()[1]].append(k)
        elif candidates.keys()[1] in v:
            if v[candidates.keys()[1]] > 0:
                stats_[candidates.keys()[1]].append(k)
            elif v[candidates.keys()[1]] < 0:
                stats_[candidates.keys()[0]].append(k)

    return stats_

def save_json(data, file):
    try:
        data_file = open(file, 'w')
        json.dump(data, data_file)
    except Exception as e:
        raise e
    else:
        data_file.close()

if __name__ == '__main__':
    import sys
    corpus = MyCorpus(sys.argv[1])
    author_id, comments = zip(*corpus)
    print "totally %s comments" % len(comments)
