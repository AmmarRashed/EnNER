import argparse


def get_accuracy(output):
    """
    :param output: output file path (formatted as: Word feature-1 ... feature-n Actual-label Predicted-label)
    :return: CoNLL, muc, muc_text, muc_type
    """
    CoNLL = 0
    muc_text = 0
    muc_type = 0
    count = 0.
    with open(output, 'r', encoding='ISO-8859-1') as f:
        for l in f:
            try:
                actual, predicted = l.strip().split("\t")[-2:]
            except ValueError:
                continue
            count += 1

            try:
                actual_location, actual_type = actual.split("-")
                predicted_location, predicted_type = predicted.split("-")
            except ValueError: # if the tag is O for example
                actual_location = predicted_location = actual_type = predicted_type = 0

            CoNLL += int(actual == predicted)

            muc_text += int(actual_location == predicted_location)
            muc_type += int(actual_type == predicted_type)

    muc = (muc_text + muc_type)/2.
    return CoNLL/count, muc/count, muc_text/count, muc_type/count


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("o", help="output file")
    args = parser.parse_args()
    output = args.o

    conll, muc, muc_text, muc_type = get_accuracy(output)
    print("CoNLL:\t\t{0}\nmuc:\t\t{1}\nmuc_text:\t{2}\nmuc_type:\t{3}".format(
        conll, muc, muc_text, muc_type
    ))