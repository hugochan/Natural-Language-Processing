import sys


if __name__ == '__main__':
    usage_line = 'python prepare_for_libsvm.py [train_path] [test_feature_path] [test_tagger_path] [out_train_path] [out_test_path]'
    try:
        train_path = sys.argv[1]
        test_feature_path = sys.argv[2]
        test_tagger_path = sys.argv[3]
        out_train_path = sys.argv[4]
        out_test_path = sys.argv[5]
    except:
        print usage_line
        sys.exit()

    # extract from training and test sets
    label_list = ['O', 'B-GPE', 'B-ORG', 'I-PER', 'I-ORG', 'B-PER', 'I-GPE']
    pos_list = ['PRP$', 'VBG', 'VBD', '``', 'POS', "''", 'VBP', 'WDT', 'JJ', 'WP', 'VBZ', 'DT', 'RP', '$', 'NN', ')', '(', 'FW', ',', '.', 'TO', 'PRP', 'RB', ':', 'NNS', 'NNP', 'VB', 'WRB', 'CC', 'PDT', 'RBS', 'RBR', 'VBN', 'EX', 'IN', 'WP$', 'CD', 'MD', 'NNPS', 'JJS', 'JJR', 'SYM', 'UH']
    label_dict = dict(zip(label_list, range(len(label_list))))
    pos_dict = dict(zip(pos_list, range(len(pos_list))))

    f1 = open(train_path, 'r')
    f2 = open(out_train_path, 'w')
    for line in f1:
        line = line.strip('\n ').split()
        label = label_dict[line[-1]] if line[-1] in label_dict else 0
        line[0] = pos_dict[line[0]] if line[0] in pos_dict else len(pos_list)
        f2.write("{} {}\n".format(label, ' '.join(['%s:%s'%(idx, line[idx]) for idx in range(len(line[:-1]))])))
    f1.close()
    f2.close()


    f3 = open(test_feature_path, 'r')
    f4 = open(test_tagger_path, 'r')
    f5 = open(out_test_path, 'w')
    for line in f3:
        line = line.strip('\n ').split()
        label = f4.readline().strip('\n ')
        label = label_dict[label] if label in label_dict else 0
        line[0] = pos_dict[line[0]] if line[0] in pos_dict else len(pos_list)
        f5.write("{} {}\n".format(label, ' '.join(['%s:%s'%(idx, line[idx]) for idx in range(len(line))])))
    f3.close()
    f4.close()
    f5.close()
