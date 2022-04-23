# launch testing scripts on local machine:
cat partA_1.txt | python mapper.py | sort | python reducer.py

# get dataset files from hadoop client machine:
scp bdb2c2022q2_Leshchankin@brain-client.bigdatateam.org:/home/group_bdb2c2022q2/bdb2c2022q2_Leshchankin/partA_1.txt "/users/alekseyleshchankin"
sftp bdb2c2022q2_Leshchankin@brain-client.bigdatateam.org:/home/group_bdb2c2022q2/bdb2c2022q2_Leshchankin/partA_1.txt
