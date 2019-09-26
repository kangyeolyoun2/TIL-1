# How To Install Apache-Spark

### 1. Install JAVA8
--------------------
brew install java8 # spark require only java8 version.

**on terminal** : environment path setting

cd /Library/Java/JavaVirtualMachines
ls # check jdk file
vi ~/.bash_profile
```
JAVA_HOME=/Library/Java/JavaVirtualMachines/adoptopenjdk-8.jdk/Contents/Home
PATH=$PATH:$JAVA_HOME/bin
export JAVA_HOME
export PATH
```

java -version # check java version

### 2. Install Spark
---------------------
brew install apache-spark

### 3. we use data in data-engineering study
-------------------------------------------- 
https://github.com/FVBros/Spark-The-Definitive-Guide
