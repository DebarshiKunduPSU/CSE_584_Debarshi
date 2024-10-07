# Midterm Project
> Debarshi Kundu (dqk5620@psu.edu)
> 
Steps to reproduce results.
### **Installation**

```shell
pip install -r requirements.txt
```
### **Dataset generation**.
Generate ($x_i$)
```shell
python3 truncated_input_generation.py
```
Run `dataset_generation.ipynb` to generate the completions ($x_j$).

### **Model**
Run `main.ipynb` to generate the classifier results.