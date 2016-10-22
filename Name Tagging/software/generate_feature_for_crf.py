# -*- coding: utf-8 -*-
import sys
import chardet
from nltk.tag import pos_tag
from nltk.tokenize import sent_tokenize
from utilities import *

def get_data_set(data_path):
    text = []
    taggers = []
    try:
        with open(data_path, 'r') as f:
            for line in f:
                data = line.strip('\n ').split()
                if not data:
                    continue
                text.append(data[0])
                taggers.append(data[1])
    except Exception as e:
        print e
        return
    else:
        f.close()
    return text, taggers



def extract_features(text):
    """
    features: pos_tagging   contains_name    contains_nationality     contains_location
            is_first_word    is_upper_case    is_title_case  is_pre_upper_or_title
            has_hyphen
    """
    features = []
    pos_list = pos_tag(text)
    sentences = sent_tokenize(' '.join(text))

    ctr = 0
    for sent in sentences:
        sent = sent.split()
        for i in range(len(sent)):
            ft = []
            ft.append(pos_list[ctr][1]) # pos_tagging
            ft.append('contains_name' if contains_name(sent[i]) else '') # contains_name
            ft.append('contains_nationality' if contains_nationality(sent[i]) else '') # contains_nationality
            ft.append('contains_location' if contains_location(sent[i]) else '') # contains_location
            ft.append('is_first_word' if i == 0 else '') # is_first_word
            ft.append('is_upper_case' if sent[i].isupper() else '') # is_upper_case
            ft.append('is_title_case' if sent[i].istitle() else '') # is_title_case
            ft.append('is_pre_upper_or_title' if i > 0 and (sent[i-1].isupper() or sent[i-1].istitle()) else '') # is_pre_upper_or_title
            ft.append('has_hyphen' if '-' in sent[i] else '') # has_hyphen
            features.append(ft)
            ctr += 1
    assert ctr == len(text)
    return features

def write_to_train_file(train_features, taggers, out_train_path):
    try:
        with open(out_train_path, 'w') as f:
            for i in range(len(train_features)):
                f.write("{} {}\n".format(' '.join(train_features[i]), taggers[i]))
    except Exception as e:
        print e
        return
    else:
        f.close()

def write_to_test_file(test_features, taggers, out_test_feature_path, out_test_tagger_path):
    try:
        f1 = open(out_test_feature_path, 'w')
        f2 = open(out_test_tagger_path, 'w')
        for i in range(len(test_features)):
            f1.write("{}\n".format(' '.join(test_features[i])))
            f2.write("{}\n".format(taggers[i]))
    except Exception as e:
        print e
        return
    else:
        f1.close()
        f2.close()


if __name__ == '__main__':
    usage_line = "run generate_features.py [train_path] [test_path] [out_train_path] [out_test_feature_path] [out_test_tagger_path]"
    try:
        train_path = sys.argv[1]
        test_path = sys.argv[2]
        out_train_path = sys.argv[3]
        out_test_feature_path = sys.argv[4]
        out_test_tagger_path = sys.argv[5]
    except:
        print usage_line
        sys.exit()
    # import pdb;pdb.set_trace()
    # get data sets
    train_set = get_data_set(train_path)
    test_set = get_data_set(test_path)
    # extract features
    train_features = extract_features(train_set[0])
    test_features = extract_features(test_set[0])

    # save to files
    write_to_train_file(train_features, train_set[1], out_train_path)
    write_to_test_file(test_features, test_set[1], out_test_feature_path, out_test_tagger_path)


