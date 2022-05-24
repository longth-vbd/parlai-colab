# parlai-colab

## Setup
1. Miniconda
```bash
sh setup/conda-install.sh
. setup/conda-create.sh
. setup/conda-activate.sh
```

2. torch
```bash
conda install pytorch==1.10.1 torchvision==0.11.2 torchaudio==0.10.1 cudatoolkit=11.3 -c pytorch -c conda-forge
```

3. parlai
```bash
pip install parlai
pip install subword_nmt
```

## Run
1. Chatting with a model
```bash
python -m parlai.scripts.interactive --model-file zoo:tutorial_transformer_generator/model
```
- Or
```bash
python scripts/chat_interactive.py
```

2. Data looking
```bash
python scripts/data_look.py
python -m parlai.scripts.display_data --task empathetic_dialogues
python -m parlai.scripts.display_data -t empathetic_dialogues
```

3. Training
```bash
rm -rf from_scratch_model
mkdir -p from_scratch_model
python scripts/train_model.py
```