# Named Entity Recognition (NER)
### Using Conditional Random Fields (CRF)

<img src="https://github.com/AmmarRashed/NER/blob/master/REX-hero.png?raw=true" width=600>

## Libraries:
-  <a href="https://taku910.github.io/crfpp/">CRF++: Yet Another CRF toolkit</a>
-  <a href="https://pandas.pydata.org/">Pandas</a>
-  <a href="http://www.numpy.org/"> NumPy</a>

## Usage:
-  `$ crf_learn template_file train_file model_file`
-  `$ crf_test -m model_file test_files`
-  `$ python accuracy.py output_file`

## Results format:
-  output file: Word feature-1 ... feature-n Actual-label Predicted-label
-  evaluation metrics:
    - CoNLL:		0.904
    - muc:		0.9575
    - muc_text:	0.963
    - muc_type:	0.952
