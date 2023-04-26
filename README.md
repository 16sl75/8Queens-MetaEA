# 8Queens-MetaEA
8 Queens Problem using Meta EA Algorithm\
The environment we are using:

Ubuntu 20.04\
Python 3.8\
cuda_11.8\
Pytorch 1.13.1\
Tensorflow 2.8.0


If you want to apply our meta EA model on 8 Queens Problem, you need to first get to the directory.
Then run
```
python3 meta_main.py
```

If you want to apply the meta EA model on Neural Netword, change the command line to
```
python3 meta_main_NN.py
```

If you want to apply the meta EA model on Reinforcement Learning, change the command line to
```
python3 meta_main_RL.py
```

After the EA algorithm is finished, the result would be stored in the corresponding .json file.
