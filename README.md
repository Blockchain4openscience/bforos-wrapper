# bforos-wrapper
CLI wrapper to track Open Science apps using BFOROS

## How it works?

The wrapper take as parameters the command or application to be wrapped and the parameters for the execution of that command and then it:

1. Runs the app with the '-v' flag
2. Parses the version message to obtain the App name, App version and the App BFOROS id. The version message has to follow this pattern:

```
<app_name> v <app version>
BFOROS Id: <BFOROS asset ID>
```

5. Sends a request to the hyperledger  REST api in order to register the usage transaction
6. Runs the wrapped app with the respective arguments

## How tu run it

### Requirements

*   Python 3.7.0+

### Instructions

1.  Go to https://bforos.blockchain4openscience.com/login and click on:​

![alt_text](https://gist.githubusercontent.com/ficolo/ba1557b45d75613cf7b5cacc61f8dbf6/raw/f45128a3a5647919e421d1945a0c9339246e5896/BFOROS-Wrapper-0.png "image_tooltip")


2.  Follow ORCID instructions to authenticate using your orcid account and authorize the app:


![alt_text](https://gist.githubusercontent.com/ficolo/ba1557b45d75613cf7b5cacc61f8dbf6/raw/f45128a3a5647919e421d1945a0c9339246e5896/BFOROS-Wrapper-1.png "image_tooltip")


3.  Click on the search Research Object button:


![alt_text](https://gist.githubusercontent.com/ficolo/ba1557b45d75613cf7b5cacc61f8dbf6/raw/f45128a3a5647919e421d1945a0c9339246e5896/BFOROS-Wrapper2.png "image_tooltip")


4.  Click on the connect to Github button:


![alt_text](https://gist.githubusercontent.com/ficolo/ba1557b45d75613cf7b5cacc61f8dbf6/raw/f45128a3a5647919e421d1945a0c9339246e5896/BFOROS-Wrapper3.png "image_tooltip")


5.  Authenticate using your github account:


![alt_text](https://gist.githubusercontent.com/ficolo/ba1557b45d75613cf7b5cacc61f8dbf6/raw/f45128a3a5647919e421d1945a0c9339246e5896/BFOROS-Wrapper-4.png "image_tooltip")


6.  Select any repository and claim it:


![alt_text](https://gist.githubusercontent.com/ficolo/ba1557b45d75613cf7b5cacc61f8dbf6/raw/f45128a3a5647919e421d1945a0c9339246e5896/BFOROS-Wrapper-5.png "image_tooltip")


7.  Clone the BFOROS wrapper repo:

    ```
    git clone https://github.com/Blockchain4openscience/bforos-wrapper.git
    cd bforos-wrapper
    ```


8.  Modify the dummy script **<code>bforos-wrapper/tests/foo.py </code></strong>in order to match the claimed app info:

 
![alt_text](https://gist.githubusercontent.com/ficolo/ba1557b45d75613cf7b5cacc61f8dbf6/raw/f45128a3a5647919e421d1945a0c9339246e5896/BFOROS-Wrapper-6.png "image_tooltip")


9.  Run the dummy script **<code>bforos-wrapper/tests/foo.py </code></strong>using the wrapper and some dummy parameters:

    ```
    python bforos-run.py ./tests/foo.py parameter1 parameter2
    ```


10.  Check the **<code>CountRO</code></strong> transaction log in [https://hyperledger.blockchain4openscience.com/explorer/#!/CountRO/CountRO_find](https://hyperledger.blockchain4openscience.com/explorer/#!/CountRO/CountRO_find):


![alt_text](https://gist.githubusercontent.com/ficolo/ba1557b45d75613cf7b5cacc61f8dbf6/raw/f45128a3a5647919e421d1945a0c9339246e5896/BFOROS-Wrapper-7.png "image_tooltip")


11.  Validate that your **<code>CountRO</code></strong> (usage transaction) was applied:


![alt_text](https://gist.githubusercontent.com/ficolo/ba1557b45d75613cf7b5cacc61f8dbf6/raw/f45128a3a5647919e421d1945a0c9339246e5896/BFOROS-Wrapper-8.png "image_tooltip")


12.  Go to BFOROS frontend at [https://bforos.blockchain4openscience.com/home/research_obj](https://bforos.blockchain4openscience.com/home/research_obj) and check the updated value in the count field of the Research Object:

![alt_text](https://gist.githubusercontent.com/ficolo/ba1557b45d75613cf7b5cacc61f8dbf6/raw/f45128a3a5647919e421d1945a0c9339246e5896/BFOROS-Wrapper-9.png "image_tooltip")
