# API

test case

1. happy case
   step 1: set param is 'animal_type': 'cat', 'amount': '1'
   step 2: send api /facts
   step 3: check status code is 200 and response is not None

2. animal_type is illegal case
   step 1: set 'animal_type' is 'horse'
   step 2: send api /facts
   step 3: check status code is 400 and response is not None

3. amount is illegal case
   step 1: set 'amount' is '0'
   step 2: send api /facts
   step 3: check status code is 400 and response is not None
   
![image](https://github.com/Annatyt1/API/assets/165688320/5bf21e38-399f-469b-a7af-89a2a01a4de2)
