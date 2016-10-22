import sys


if __name__ == '__main__':
    usage_line = 'python prepare_for_srfsuite.py []'
    try:
        train_path = sys.argv[1]
        test_feature_path = sys.argv[2]
        test_tagger_path = sys.argv[3]
        out_train_path = sys.argv[4]
        out_test_path = sys.argv[5]
    except:
        print usage_line
        sys.exit()

    f1 = open(train_path, 'r')
    f2 = open(out_train_path, 'w')
    for line in f1:
        line = line.strip('\n ').split()
        f2.write("{} {}\n".format(line[-1], ' '.join(line[:-1])))
    f1.close()
    f2.close()


    f3 = open(test_feature_path, 'r')
    f4 = open(test_tagger_path, 'r')
    f5 = open(out_test_path, 'w')
    for line in f3:
        line = line.strip('\n ')
        tagger = f4.readline().strip('\n ')
        f5.write("{} {}\n".format(tagger, line))
    f3.close()
    f4.close()
    f5.close()
