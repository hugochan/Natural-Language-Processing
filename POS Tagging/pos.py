import sys
from collections import defaultdict

def read_data(file):
    emiss_dict = defaultdict(dict)
    trans_dict = defaultdict(dict)
    try:
        with open(file, 'r') as f:
            for line in f:
                if line == '\r\n':
                    continue
                new_line = line.strip(' \r\n').split()
                pre_pos = 'start'
                for each in new_line:
                    word, pos = each.split('/')
                    # count emission and transition
                    try:
                        emiss_dict[pos][word] += 1.0
                        trans_dict[pre_pos][pos] += 1.0
                    except:
                        emiss_dict[pos][word] = 1.0
                        trans_dict[pre_pos][pos] = 1.0
                    pre_pos = pos
                try:
                    trans_dict[pre_pos]['end'] += 1.0
                except:
                    trans_dict[pre_pos]['end'] = 1.0
    except Exception as e:
        print e
        sys.exit()
    else:
        f.close()
    return emiss_dict, trans_dict

def calc_emiss_prob(emiss_dict):
    emiss_prob = defaultdict(dict)
    for pos, val in emiss_dict.iteritems():
        sum_ = sum(val.values())
        for word, count in val.iteritems():
            emiss_prob[pos][word] = count / sum_
    emiss_prob['end'] = {}
    return emiss_prob

def calc_trans_prob(trans_dict):
    trans_prob = defaultdict(dict)
    for pos, val in trans_dict.iteritems():
        sum_ = sum(val.values())
        for next_pos, count in val.iteritems():
            trans_prob[pos][next_pos] = count / sum_
    return trans_prob

def viterbi(string, emiss_prob, trans_prob):
    pos_tags = []
    cur_pos = 'start'
    for word in string:
        possible_probs = [(next_pos, prob * (emiss_prob[next_pos][word] if emiss_prob[next_pos].has_key(word) else 0)) for next_pos, prob in trans_prob[cur_pos].iteritems()]
        try:
            cur_pos, prob = sorted(possible_probs, key=lambda d:d[1], reverse=True)[0]
        except:
            print "PARSE ERROR!"
            sys.exit()
        else:
            if prob == 0:
                # we simply choose the most popular pos tag of that word
                try:
                    cur_pos = sorted([(pos, val[word]) for pos, val in emiss_prob.iteritems() if word in val.keys()], \
                        key=lambda d: d[1], reverse=True)[0][0]
                except:
                    # we simply choose the most likely next state (POS tag) as the tag of an OUT of VOCABULARY word
                    cur_pos = sorted(trans_prob[cur_pos].items(), key=lambda d: d[1], reverse=True)[0][0]

        pos_tags.append(cur_pos)
    return pos_tags

def naive_base(string, emiss_prob):
    pos_tags = []
    for word in string:
        # we simply choose the most popular pos tag of that word
        try:
            cur_pos = sorted([(pos, val[word]) for pos, val in emiss_prob.iteritems() if word in val.keys()], \
                key=lambda d: d[1], reverse=True)[0][0]
        except:
            # we simply choose NN as the tag of an OUT of VOCABULARY word
            cur_pos = 'NN'
        pos_tags.append(cur_pos)
    return pos_tags

# for test functions
def read_test_data(file):
    try:
        with open(file, 'r') as f:
            test = [line for line in f]
    except Exception as e:
        print e
        sys.exit()
    else:
        f.close()
    return test

def stem_helper(test):
    word_test = []
    pos_test = []
    for string in test:
        # parse a bag of words and the corresponding pos taggs from a labled sentence
        words, poses = zip(*[each.split('/') for each in string.strip(' \r\n').split()])
        word_test.append(words)
        pos_test.append(poses)
    return word_test, pos_test

def calc_accuracy(pred, truth):
    return sum([pred[i] == truth[i] for i in range(len(pred))]) / float(len(pred))

if __name__ == "__main__":
    try:
        train_data = sys.argv[1]
        test_data = sys.argv[2]
    except:
        train_data = "wsj_pos/training.txt"
        test_data = "wsj_pos/test.txt"
    emiss_dict, trans_dict = read_data(train_data)
    emiss_prob = calc_emiss_prob(emiss_dict)
    trans_prob = calc_trans_prob(trans_dict)

    test = read_test_data(test_data)
    word_test, pos_test = stem_helper(test)

    print "viterbi algorithm:"
    acc = 0.0
    for i in range(len(word_test)):
        pos_tags = viterbi(word_test[i], emiss_prob, trans_prob)
        print "test case %s)" % i
        print word_test[i]
        print "prediction:"
        print pos_tags
        print "ground truth:"
        print pos_test[i]
        print
        acc += calc_accuracy(pos_tags, pos_test[i])
    print "average error rate: %s\n" % (1 - (acc / len(word_test)))

    print "frequency-based naive algorithm:"
    acc = 0.0
    for i in range(len(word_test)):
        pos_tags = naive_base(word_test[i], emiss_prob)
        print "test case %s)" % i
        print word_test[i]
        print "prediction:"
        print pos_tags
        print "ground truth:"
        print pos_test[i]
        print
        acc += calc_accuracy(pos_tags, pos_test[i])
    print "average error rate: %s\n" % (1 - (acc / len(word_test)))
