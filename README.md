# tealeavesfunc

1. Clone this repo in VS Code

2. Activate Python Environment

``` source srienv/bin/activate```

3. Follow the steps to create the function https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python 
Select the current folder for Function Apps

4. Modify the __init__.py file to do the prediction code

5. To run a local server, in terminal type: 

``` func start ```

6. Using postman or any way, send an Image through POST method to https://localhost:7071/api/predict


7. To deploy to azure function, follow the above documentation
