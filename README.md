# Port Sucker

![image](https://user-images.githubusercontent.com/85181215/139897509-86e366d4-f5bf-4dc8-b113-e580d26c2b4d.png)

------
## Description:

Port Sucker is a Port Scanning Tool That will use to find open port of the target system/computer.
This is a fast Port Scanning tool that will show you all open port as soon as posible. The time
depends on the target system distance and connection speed but they will provide you best result as they can

## Installation

> - Download the Project
> After Downloading install the requirments using the following command
```
pip3 install -r requirments.txt
```
> This will download all the requirments for this tool and now you are good to go for use this tool
```
$ python3 PortSucker.py
```

## Usage

To use PortSucker you have to download the script first and make sure all the requirement is satisfied after that you have to
you can run the script with the following command.
```
$ python3 portSucker.py
```
If every thing write this will show you the syntax how to specify data to the the tool like follows

![image](https://user-images.githubusercontent.com/85181215/139906965-c7390169-0ed3-4148-a4e6-b68ab3321607.png)

There you will see They show us the following Syntax
```
PortSucker.py [Target IP Address] [Starting Port Range No] [Ending Port Range No]
```
When we follow the syntax Properly we will able to scan any target we specify

## Examples

```
$ python3 PortSucker.py 192.168.10.1 1 100
```
```
$ python3 PortSucker.py www.example.com 1 100

```
This also give us to specify multiple Targets to do that we just have to separate other targets by **Comma(,) Like follows
```
$ python3 PortSucker.py 192.168.10.1,www.example.com,10.10.10.10 1 100
```

![image](https://user-images.githubusercontent.com/85181215/139909525-8f1fc4d5-2069-423c-825e-297bcfddd56b.png)
