import tensorflow as tf
import data_utils
import seq2seq_model

## preperation for dataset
def train():
    encTrain, decTrain = data_utils.prepare_custom_data(gConfig['working directory'])

    trainSet = readData(encTrain, decTrain)

## imbed input
def seq2seq_f(encoderInputs, decoderInputs, doDecode):
    return tf.nn.seq2seq.embedding_attention_seq2seq(
        encoderInputs, decoderInputs, cell,
        numEncoderSymbols = sourceVocabSize,
        numDecoderSymbols = targetVocabSize,
        embeddingSize = size,
        outputProjection = outputProjection,
        feedPrevious = doDecode)

## create model
with tf.Session(config=config) as sess:
    model = create_model(sess, False)

    ## run computation graph
    while True:
        sess.run(model)

        ## save checkpt, zero-timer, loss
        checkpointPath = os.path.join(gConfig['working_directory'], "seq2seq.ckpt")
        model.saver.save(sess, checkpointPath, global_step=model.global_step)
