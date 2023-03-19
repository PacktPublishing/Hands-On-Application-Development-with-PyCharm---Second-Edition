from tqdm import tqdm
from time import sleep

text = ""
for char in tqdm(["a", "b", "c", "d"]):
    mispeld = "this is not spelled correctly"
    sleep(0.25)
    text = text + char

