# aridhia-git-tag-upload
Repository with the required files to create a githook to upload files to Aridhia upon git push.

### **IMPORTANT**
Always add your .aridhia_secret.json file to your .gitignore otherwise you risk exposing your API key

### Setup
This project requires Python 3 to be installed and has been developed for macosX.

Steps to setup for a specific project repo:
- Clone this repository or download the files
- Copy the file "ApiCommunicator.py" to the following folder within your project repo /.git/hooks
- Copy the file "pre-push" to the following folder within your project repo /.git/hooks
- Copy the ".aridhia_secret.json" to the top level of your project repo
- Add your Aridhia data upload API key to the ".aridhia_secret.json" file
- ADD .aridhia_secret.json TO YOUR GITIGNORE FILE