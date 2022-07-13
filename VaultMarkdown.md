####**Utilizing the HVAC package to operate Vault in Python**
1. Creating an Environment  
  Open an Anaconda Prompt  
  Use command "conda create -n _nameOfEnvironment_ python"  
  When asked to proceed enter "y"  
  Activate the environment with command "conda activate _nameOfEnvironment_"  
  With the environment activated, enter "pip install hvac"

2. [Downloading Vault](https://learn.hashicorp.com/tutorials/vault/getting-started-install?in=vault/getting-started)  
3. Starting the Vault Server  
  Open Git Bash  
  Enter "vault server -dev -dev-root-token-id="dev-only-token""  
    * -dev-root-token-id flag allows full root access to anyone who presents the token. If the toekn name is changed make sure you change it within the code.


4. Connect the IDE to the environment  
  [Configure a Virtual Environment for Pycharm](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html)  
  [Configure a Virtual Environment for Spyder](https://medium.com/analytics-vidhya/5-steps-setup-python-virtual-environment-in-spyder-ide-da151bafa337)

5. Run Code