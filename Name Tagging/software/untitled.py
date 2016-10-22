import sys

if __name__ == '__main__':
    test_path = sys.argv[1]
    pred_path = sys.argv[2]
    out_path = sys.argv[3]
    try:
        f1 = open(test_path, 'r')
        f2 = open(pred_path, 'r')
        f3 = open(out_path, 'w')

        for line in f1:
            label = line.strip('\n ').split()
            pred = f2.readline().strip('\n ')
            if not label:
                f3.write('\n')
                continue
            f3.write('%s %s\n'%(' '.join(label[:-1]), pred))

    except Exception as e:
        print e
        sys.exit()
    else:
        f1.close()
        f2.close()
        f3.close()
