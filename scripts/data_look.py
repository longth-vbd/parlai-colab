# The display_data script is used to show the contents of a particular task.
# By default, we show the train
from parlai.scripts.display_data import DisplayData
DisplayData.main(task='empathetic_dialogues', num_examples=5)

# we can instead ask to see fewer examples, and get them from the valid set.
DisplayData.main(task='empathetic_dialogues', num_examples=3, datatype='valid')