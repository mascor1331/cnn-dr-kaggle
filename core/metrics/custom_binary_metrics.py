
import keras.backend as K

def tp(y_true, y_pred):
    return K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))

def fp(y_true, y_pred):
    return K.sum(K.round(K.clip(y_pred, 0, 1))) - K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))

def fn(y_true, y_pred):
    return K.sum(K.round(K.clip(y_true, 0, 1))) - K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))

# TODO: def tn(y_true, y_pred):



def precision(y_true, y_pred):
    """Precision metric.

    Only computes a batch-wise average of precision.

    Computes the precision, a metric for multi-label classification of
    how many selected items are relevant.
    """
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    return (true_positives / (predicted_positives + K.epsilon()))




def recall(y_true, y_pred):
    """Recall metric.

    Only computes a batch-wise average of recall.

    Computes the recall, a metric for multi-label classification of
    how many relevant items are selected.
    """
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    return (true_positives / (possible_positives + K.epsilon()))




def f1(y_true, y_pred):
    pr = precision(y_true, y_pred)
    re = recall(y_true, y_pred)
    return 2*((pr * re)/(pr + re + K.epsilon()))




def mcc(y_true, y_pred):
    """ Matthews Correlation Coefficient.


    """
    y_pred_pos = K.round(K.clip(y_pred, 0, 1))
    y_pred_neg = 1 - y_pred_pos

    y_pos = K.round(K.clip(y_true, 0, 1))
    y_neg = 1 - y_pos

    tp = K.sum(y_pos * y_pred_pos)
    tn = K.sum(y_neg * y_pred_neg)

    fp = K.sum(y_neg * y_pred_pos)
    fn = K.sum(y_pos * y_pred_neg)

    numerator = (tp * tn - fp * fn)
    denominator = K.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))

    return numerator / (denominator + K.epsilon())
    



def auc(y_true, y_pred):

    return 1