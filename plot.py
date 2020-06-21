import re
d = """
Epoch 0/24
----------
train Loss: 1.0481 Acc: 0.5227
val Loss: 1.3091 Acc: 0.5419

Epoch 1/24
----------
train Loss: 0.8205 Acc: 0.6347
val Loss: 1.1673 Acc: 0.5831

Epoch 2/24
----------
train Loss: 0.7236 Acc: 0.6829
val Loss: 0.8747 Acc: 0.5824

Epoch 3/24
----------
train Loss: 0.6243 Acc: 0.7393
val Loss: 0.8566 Acc: 0.6654

Epoch 4/24
----------
train Loss: 0.5647 Acc: 0.7621
val Loss: 1.2468 Acc: 0.6243

Epoch 5/24
----------
train Loss: 0.4926 Acc: 0.7943
val Loss: 1.2975 Acc: 0.6088

Epoch 6/24
----------
train Loss: 0.4414 Acc: 0.8156
val Loss: 1.1614 Acc: 0.6103

Epoch 7/24
----------
train Loss: 0.2994 Acc: 0.8812
val Loss: 1.2108 Acc: 0.6743

Epoch 8/24
----------
train Loss: 0.2731 Acc: 0.8926
val Loss: 1.0931 Acc: 0.6838

Epoch 9/24
----------
train Loss: 0.2531 Acc: 0.9004
val Loss: 1.1579 Acc: 0.6676

Epoch 10/24
----------
train Loss: 0.2423 Acc: 0.9029
val Loss: 1.1264 Acc: 0.6574

Epoch 11/24
----------
train Loss: 0.2267 Acc: 0.9088
val Loss: 1.1696 Acc: 0.6765

Epoch 12/24
----------
train Loss: 0.2099 Acc: 0.9183
val Loss: 1.1444 Acc: 0.6846

Epoch 13/24
----------
train Loss: 0.2058 Acc: 0.9178
val Loss: 1.1155 Acc: 0.6794

Epoch 14/24
----------
train Loss: 0.2028 Acc: 0.9226
val Loss: 1.1092 Acc: 0.6809

Epoch 15/24
----------
train Loss: 0.2010 Acc: 0.9192
val Loss: 1.1313 Acc: 0.6809

Epoch 16/24
----------
train Loss: 0.1914 Acc: 0.9261
val Loss: 1.1365 Acc: 0.6816

Epoch 17/24
----------
train Loss: 0.2045 Acc: 0.9184
val Loss: 1.1386 Acc: 0.6809

Epoch 18/24
----------
train Loss: 0.1957 Acc: 0.9242
val Loss: 1.1840 Acc: 0.6618

Epoch 19/24
----------
train Loss: 0.1981 Acc: 0.9227
val Loss: 1.1655 Acc: 0.6772

Epoch 20/24
----------
train Loss: 0.1928 Acc: 0.9236
val Loss: 1.1869 Acc: 0.6537

Epoch 21/24
----------
train Loss: 0.1974 Acc: 0.9227
val Loss: 1.1636 Acc: 0.6735

Epoch 22/24
----------
train Loss: 0.1904 Acc: 0.9253
val Loss: 1.1176 Acc: 0.6846

Epoch 23/24
----------
train Loss: 0.1916 Acc: 0.9261
val Loss: 1.1870 Acc: 0.6654

Epoch 24/24
----------
train Loss: 0.1955 Acc: 0.9250
val Loss: 1.1175 Acc: 0.6816

Training complete in 36m 22s
Best val Acc: 0.684559
"""

# groups = re.findall('train Loss: (.+) Acc: (.+)', d)
groups = re.findall('val Loss: (.+) Acc: (.+)', d)

i = 0
for group in groups:
    print(str(i) + ',' + group[0] + ','+group[1])
    i+=1

# print(groups)
