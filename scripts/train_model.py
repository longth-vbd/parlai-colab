# we'll save it in the "from_scratch_model" directory

from parlai.scripts.train_model import TrainModel

TrainModel.main(
    # we MUST provide a filename
    model_file='from_scratch_model/model',
    # train on empathetic dialogues
    task='empathetic_dialogues',
    # limit training time to 2 minutes, and a batchsize of 16
    max_train_time=2 * 60,
    batchsize=16,

    # we specify the model type as seq2seq
    model='seq2seq',
    # some hyperparamter choices. We'll use attention. We could use pretrained
    # embeddings too, with embedding_type='fasttext', but they take a long
    # time to download.
    attention='dot',
    # tie the word embeddings of the encoder/decoder/softmax.
    lookuptable='all',
    # truncate text and labels at 64 tokens, for memory and time savings
    truncate=64,
)