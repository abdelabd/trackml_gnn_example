### From: https://github.com/GageDeZoort/interaction_network_paper


### Construct graphs
python build_heptrkx_plus.py heptrkx_plus.py


### Build and train model, convert with torchscript, compare normal model with torchscript model
python run_interaction_network.py --pt=1 --construction=heptrkx_plus --lr=0.01 --gamma=0.5 --save-model
