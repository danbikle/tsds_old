# tf03.py

# This script should use TensorFlow to predict S&P500.

# Demo:
# python tf03.py


import tensorflow.python.platform

import numpy      as np
import tensorflow as tf
import pandas     as pd
import pdb

# Global variables.
NUM_LABELS = 2    # The number of labels.
BATCH_SIZE = 100  # The number of training examples to use per training step.

# Define the flags useable from the command line.
tf.app.flags.DEFINE_string('train', None,
                           'File containing the training data (labels & features).')
tf.app.flags.DEFINE_string('test', None,
                           'File containing the test data (labels & features).')
tf.app.flags.DEFINE_integer('num_epochs', 1,
                            'Number of passes over the training data.')
tf.app.flags.DEFINE_integer('num_hidden', 1,
                            'Number of nodes in the hidden layer.')
tf.app.flags.DEFINE_boolean('verbose', False, 'Produce verbose output.')
FLAGS   = tf.app.flags.FLAGS
verbose = FLAGS.verbose

# I should use Pandas and Numpy here:
data_df  = pd.read_csv('http://www.spy611.com/csv/allpredictions.csv')
train_sr = (data_df['cdate'] > '2010') & (data_df['cdate'] < '2016')
test_sr  =  data_df['cdate'] > '2016'
train_df = data_df[['actual_dir', 'pctlag1', 'pctlag2', 'pctlag4', 'pctlag8', 'pctlag16']][train_sr]
test_df  = data_df[['actual_dir', 'pctlag1', 'pctlag2', 'pctlag4', 'pctlag8', 'pctlag16']][test_sr]
train_a  = np.array(train_df)
test_a   = np.array(test_df)
train_data       = train_a[:,1:].astype(np.float32)
test_data        = test_a[:,1:].astype(np.float32)
train_labels_i_a = train_a[:,0].astype(dtype=np.uint8)
test_labels_i_a  = test_a[:,0].astype(dtype=np.uint8)
# Convert the int numpy array into a one-hot matrix.
train_labels     = (np.arange(NUM_LABELS) == train_labels_i_a[:, None]).astype(np.float32)
test_labels      = (np.arange(NUM_LABELS) == test_labels_i_a[:, None]).astype(np.float32)

pdb.set_trace()
test_a[:5]
'bye'

