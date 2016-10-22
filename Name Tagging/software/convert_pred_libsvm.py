import sys

if __name__ == '__main__':
    usage_line = 'python convert_pred_libsvm.py [pred_path] [out_pred_path]'
    try:
        pred_path = sys.argv[1]
        out_pred_path = sys.argv[2]
    except:
        print usage_line
        sys.exit()

    label_list = ['O', 'B-GPE', 'B-ORG', 'I-PER', 'I-ORG', 'B-PER', 'I-GPE']
    label_dict = dict(zip(range(len(label_list)), label_list))

    f1 = open(pred_path, 'r')
    f2 = open(out_pred_path, 'w')
    pre_label = None
    for line in f1:
        line = line.strip('\n ')
        label = label_dict[int(line)] if int(line) in label_dict else 'O'
        # if label[0] == 'I' and pre_label != None and pre_label[0] != 'B' and pre_label[0] != 'I':
        f2.write("{}\n".format(label))
        pre_label = label
    f1.close()
    f2.close()
